// POST /api/call-webhook?token=SECRET : Retell AI post-call webhook -> Firestore "call_leads"
// In Retell, set the agent webhook URL to https://YOURDOMAIN/api/call-webhook?token=<CALL_WEBHOOK_TOKEN>
// and define the post-call analysis fields listed in receptionist/README.md.
import { addDoc, notify, json } from "../_lib/firestore.js";

export async function onRequestPost({ request, env }) {
  const url = new URL(request.url);
  if (!env.CALL_WEBHOOK_TOKEN || url.searchParams.get("token") !== env.CALL_WEBHOOK_TOKEN) return json({ error: "forbidden" }, 403);

  let evt;
  try { evt = await request.json(); } catch { return json({ error: "bad_request" }, 400); }
  // Only store once, when the post-call analysis is ready
  if (evt.event !== "call_analyzed") return json({ ok: true, ignored: evt.event || "unknown" });

  const call = evt.call || {};
  const a = call.call_analysis || {};
  const x = a.custom_analysis_data || {};
  const lead = {
    source: "phone",
    status: "new",
    call_id: call.call_id,
    from_number: call.from_number,
    to_number: call.to_number,
    duration_ms: Number(call.duration_ms) || undefined,
    caller_name: x.caller_name,
    company: x.company,
    callback_phone: x.callback_phone || call.from_number,
    email: x.email,
    product_interest: x.product_interest,
    quantity: x.quantity,
    application: x.application,
    ship_to_zip: x.ship_to_zip,
    wants_callback: x.wants_callback,
    urgency: x.urgency,
    summary: a.call_summary,
    sentiment: a.user_sentiment,
    transcript: typeof call.transcript === "string" ? call.transcript.slice(0, 19000) : undefined,
    recording_url: call.recording_url,
    raw_analysis: typeof a === "object" ? a : undefined, // kept whole in case field names differ
  };
  try {
    const id = await addDoc(env, "call_leads", lead, call.call_id);
    if (id === "duplicate") return json({ ok: true, duplicate: true }); // Retell retries; store once
    await notify(env, `Phone lead: ${lead.caller_name || "unknown"} ${lead.company ? "(" + lead.company + ")" : ""} ${lead.callback_phone || ""} · ${lead.product_interest || ""} · ${lead.summary || ""}`.slice(0, 1800));
    return json({ ok: true, id });
  } catch (e) {
    console.error(e);
    return json({ ok: false }, 500); // non-2xx lets Retell retry
  }
}
