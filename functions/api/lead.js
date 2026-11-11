// POST /api/lead : quote form submissions -> Firestore "leads"
import { addDoc, notify, json } from "../_lib/firestore.js";
import { sameOrigin } from "../_lib/guard.js";

const FIELDS = ["name", "company", "email", "phone", "product", "configuration", "hose_length", "quantity", "application", "message",
  "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "page",
  // first-touch attribution and the GA4 client id, filled by /assets/analytics.js, so a lead can be matched to its GA session
  "landing_page", "referrer", "first_seen", "ga_client_id", "pages_viewed"];

export async function onRequestPost({ request, env }) {
  if (!sameOrigin(request)) return json({ ok: false, error: "forbidden" }, 403);
  let data = {};
  const ct = request.headers.get("content-type") || "";
  try {
    if (ct.includes("application/json")) data = await request.json();
    else data = Object.fromEntries(await request.formData());
  } catch { return json({ ok: false, error: "bad_request" }, 400); }

  if (data.website) return json({ ok: true }); // honeypot: pretend success, store nothing
  // The page sends how long the form was open. Under 3 seconds, or no value at all, is a script: pretend success, store nothing.
  if (!(Number(data.elapsed) >= 3000)) return json({ ok: true });

  const lead = {};
  for (const k of FIELDS) if (data[k] != null) lead[k] = String(data[k]).trim().slice(0, 2000);
  if (!lead.name || !/^\S+@\S+\.\S+$/.test(lead.email || "")) return json({ ok: false, error: "name_and_email_required" }, 422);
  lead.quantity = parseInt(lead.quantity, 10) || 1;
  lead.source = "web_form";
  lead.status = "new";
  lead.ip_country = request.headers.get("cf-ipcountry") || "";

  try {
    const id = await addDoc(env, "leads", lead);
    await notify(env, `New quote request: ${lead.name} (${lead.company || "no company"}) ${lead.email} · ${lead.product || ""} ${lead.configuration} x${lead.quantity}${lead.hose_length ? " · hose: " + lead.hose_length : ""} · ${lead.application} · came from: ${lead.utm_source || lead.referrer || "direct"} → ${lead.landing_page || lead.page || "?"}`);
    return json({ ok: true, id });
  } catch (e) {
    console.error(e);
    return json({ ok: false, error: "store_failed" }, 502); // the page falls back to email
  }
}
