// POST /api/lead : quote form submissions -> Firestore "leads"
import { addDoc, notify, json } from "../_lib/firestore.js";

const FIELDS = ["name", "company", "email", "phone", "configuration", "quantity", "application", "message",
  "utm_source", "utm_medium", "utm_campaign", "utm_term", "gclid", "page"];

export async function onRequestPost({ request, env }) {
  let data = {};
  const ct = request.headers.get("content-type") || "";
  try {
    if (ct.includes("application/json")) data = await request.json();
    else data = Object.fromEntries(await request.formData());
  } catch { return json({ ok: false, error: "bad_request" }, 400); }

  if (data.website) return json({ ok: true }); // honeypot: pretend success, store nothing

  const lead = {};
  for (const k of FIELDS) if (data[k] != null) lead[k] = String(data[k]).trim().slice(0, 2000);
  if (!lead.name || !/^\S+@\S+\.\S+$/.test(lead.email || "")) return json({ ok: false, error: "name_and_email_required" }, 422);
  lead.quantity = parseInt(lead.quantity, 10) || 1;
  lead.source = "web_form";
  lead.status = "new";
  lead.ip_country = request.headers.get("cf-ipcountry") || "";

  try {
    const id = await addDoc(env, "leads", lead);
    await notify(env, `New GG20 quote request: ${lead.name} (${lead.company || "no company"}) ${lead.email} · ${lead.configuration} x${lead.quantity} · ${lead.application}`);
    return json({ ok: true, id });
  } catch (e) {
    console.error(e);
    return json({ ok: false, error: "store_failed" }, 502); // the page falls back to email
  }
}
