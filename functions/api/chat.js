// POST /api/chat : brief, grounded answers about the GG20. Env: ANTHROPIC_API_KEY (optional CHAT_MODEL).
// Leads mentioned in chat (an email address) are also saved to Firestore "chat_leads" when Firebase env is set.
import { KB } from "../_lib/kb.js";
import { addDoc, notify, json } from "../_lib/firestore.js";

const SYSTEM = `You answer questions on the website of an independent US reseller of the ELAFLEX GasGuard GG20 LPG nozzle.

Rules:
- Answer ONLY from the knowledge base below. If it isn't covered, say you don't have that detail and offer the quote form or phone.
- Be brief: 1 to 3 short sentences, then at most one link. Plain text. Links as [label](/guides/slug.html) or [quote form](/#quote).
- Never invent prices, stock, lead times, or shipping terms. For those, point to the [quote form](/#quote) or phone {{PHONE_DISPLAY}}.
- Never say the reseller is an authorized or official ELAFLEX distributor. It is independent.
- Safety: if someone describes a leak or uncontrolled gas release, tell them to release the lever, use the emergency stop, clear the area and call emergency services if needed, before anything else.
- Don't give installation or repair instructions beyond what the knowledge base says; recommend a qualified LP-gas technician and the authority having jurisdiction for code questions.
- Off-topic questions: politely say you only cover the GG20 and related GasGuard products.
- If the visitor wants to buy or gives contact details, thank them and point to the [quote form](/#quote).

KNOWLEDGE BASE:
${KB}`;

export async function onRequestPost({ request, env }) {
  if (!env.ANTHROPIC_API_KEY) return json({ reply: "Chat isn't configured yet. Please use the [quote form](/#quote) or call {{PHONE_DISPLAY}}." });
  let body;
  try { body = await request.json(); } catch { return json({ error: "bad_request" }, 400); }

  const messages = (Array.isArray(body.messages) ? body.messages : [])
    .slice(-8)
    .filter((m) => (m.role === "user" || m.role === "assistant") && typeof m.content === "string")
    .map((m) => ({ role: m.role, content: m.content.slice(0, 1000) }));
  while (messages.length && messages[0].role !== "user") messages.shift();
  if (!messages.length || messages[messages.length - 1].role !== "user") return json({ error: "no_question" }, 400);

  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({
      model: env.CHAT_MODEL || "claude-haiku-4-5-20251001",
      max_tokens: 300,
      system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
      messages,
    }),
  });
  if (!r.ok) { console.error("anthropic", r.status, await r.text()); return json({ error: "upstream" }, 502); }
  const out = await r.json();
  const reply = (out.content || []).filter((c) => c.type === "text").map((c) => c.text).join("").trim()
    || "I don't have that detail. Please use the [quote form](/#quote).";

  // Capture an email if the visitor typed one
  const last = messages[messages.length - 1].content;
  const email = (last.match(/[^\s@]+@[^\s@]+\.[^\s@]+/) || [])[0];
  if (email && env.FIREBASE_PROJECT_ID) {
    try {
      await addDoc(env, "chat_leads", { email, message: last, page: String(body.page || ""), source: "chat", status: "new" });
      await notify(env, `Chat lead: ${email} · "${last.slice(0, 200)}"`);
    } catch (e) { console.error(e); }
  }
  return json({ reply });
}
