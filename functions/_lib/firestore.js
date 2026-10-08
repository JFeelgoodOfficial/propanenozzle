// Minimal Firestore REST client for Cloudflare Pages Functions (no SDK; WebCrypto JWT signing).
// Env vars: FIREBASE_PROJECT_ID, FIREBASE_CLIENT_EMAIL, FIREBASE_PRIVATE_KEY (service account, role "Cloud Datastore User").

let cached = { token: null, exp: 0 };

const b64url = (buf) =>
  btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const b64urlStr = (s) => b64url(new TextEncoder().encode(s));

async function importKey(pem) {
  const body = pem.replace(/\\n/g, "\n").replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
  const der = Uint8Array.from(atob(body), (c) => c.charCodeAt(0));
  return crypto.subtle.importKey("pkcs8", der, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
}

export async function signJwt(env, now = Math.floor(Date.now() / 1000)) {
  const header = b64urlStr(JSON.stringify({ alg: "RS256", typ: "JWT" }));
  const claims = b64urlStr(JSON.stringify({
    iss: env.FIREBASE_CLIENT_EMAIL, sub: env.FIREBASE_CLIENT_EMAIL,
    aud: "https://oauth2.googleapis.com/token",
    scope: "https://www.googleapis.com/auth/datastore",
    iat: now, exp: now + 3600,
  }));
  const key = await importKey(env.FIREBASE_PRIVATE_KEY);
  const sig = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, new TextEncoder().encode(`${header}.${claims}`));
  return `${header}.${claims}.${b64url(sig)}`;
}

async function accessToken(env) {
  const now = Math.floor(Date.now() / 1000);
  if (cached.token && cached.exp - 60 > now) return cached.token;
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer", assertion: await signJwt(env, now) }),
  });
  if (!r.ok) throw new Error(`token ${r.status}: ${await r.text()}`);
  const j = await r.json();
  cached = { token: j.access_token, exp: now + (j.expires_in || 3600) };
  return cached.token;
}

// Convert a flat JS object into Firestore typed fields.
export function toFields(obj) {
  const f = {};
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined || v === null || v === "") continue;
    if (typeof v === "number") f[k] = Number.isInteger(v) ? { integerValue: String(v) } : { doubleValue: v };
    else if (typeof v === "boolean") f[k] = { booleanValue: v };
    else if (v instanceof Date) f[k] = { timestampValue: v.toISOString() };
    else if (typeof v === "object") f[k] = { mapValue: { fields: toFields(v) } };
    else f[k] = { stringValue: String(v).slice(0, 20000) };
  }
  return f;
}

// docId optional: when given, a repeat write with the same id returns "duplicate" instead of a second record.
export async function addDoc(env, collection, data, docId) {
  const token = await accessToken(env);
  let url = `https://firestore.googleapis.com/v1/projects/${env.FIREBASE_PROJECT_ID}/databases/(default)/documents/${collection}`;
  if (docId) url += `?documentId=${encodeURIComponent(String(docId).replace(/[^A-Za-z0-9_-]/g, "_"))}`;
  const r = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: JSON.stringify({ fields: toFields({ ...data, created_at: new Date() }) }),
  });
  if (r.status === 409) return "duplicate";
  if (!r.ok) throw new Error(`firestore ${r.status}: ${await r.text()}`);
  return (await r.json()).name;
}

// Optional: ping a Slack/Discord/ntfy-style webhook so you hear about a lead immediately.
export async function notify(env, text) {
  if (!env.NOTIFY_WEBHOOK_URL) return;
  try {
    await fetch(env.NOTIFY_WEBHOOK_URL, { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, content: text }) });
  } catch (e) { /* never block a lead on a notification */ }
}

export const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });
