// Export Firestore leads to CSV.  Usage (Node 18+):
//   FIREBASE_PROJECT_ID=... FIREBASE_CLIENT_EMAIL=... FIREBASE_PRIVATE_KEY="$(cat key.pem)" node scripts/export-leads.mjs leads > leads.csv
// Collections: leads (web form), chat_leads (chat), call_leads (phone)
import { signJwt } from "../functions/_lib/firestore.js";

const env = process.env;
const col = process.argv[2] || "leads";
const tok = await (await fetch("https://oauth2.googleapis.com/token", {
  method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({ grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer", assertion: await signJwt(env) }),
})).json();
if (!tok.access_token) { console.error(tok); process.exit(1); }

const val = (v) => v.stringValue ?? v.integerValue ?? v.doubleValue ?? v.booleanValue ?? v.timestampValue ?? (v.mapValue ? JSON.stringify(v.mapValue) : "");
const rows = []; let pageToken = "";
do {
  const u = `https://firestore.googleapis.com/v1/projects/${env.FIREBASE_PROJECT_ID}/databases/(default)/documents/${col}?pageSize=300${pageToken ? "&pageToken=" + pageToken : ""}`;
  const j = await (await fetch(u, { headers: { Authorization: `Bearer ${tok.access_token}` } })).json();
  for (const d of j.documents || []) rows.push(Object.fromEntries(Object.entries(d.fields || {}).map(([k, v]) => [k, val(v)])));
  pageToken = j.nextPageToken || "";
} while (pageToken);

const cols = [...new Set(rows.flatMap(Object.keys))].filter((c) => c !== "transcript" && c !== "raw_analysis");
const esc = (s) => `"${String(s ?? "").replace(/"/g, '""')}"`;
console.log(cols.map(esc).join(","));
for (const r of rows) console.log(cols.map((c) => esc(r[c])).join(","));
