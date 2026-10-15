// POST /api/chat : brief, grounded answers about the GG20. Env: GROQ_API_KEY (optional CHAT_MODEL).
// Leads mentioned in chat (an email address) are also saved to Firestore "chat_leads" when Firebase env is set.
import { relevantKB } from "../_lib/retrieve.js";
import { addDoc, notify, json } from "../_lib/firestore.js";

const rules = `You answer questions on the website of an independent US reseller of the ELAFLEX GasGuard GG20 LPG nozzle.

Rules:
- Answer ONLY from the knowledge base below. If it isn't covered, say you don't have that detail and offer the quote form or phone.
- Be brief: 1 to 3 short sentences, then at most one link. Plain text. Links as [label](/guides/slug.html) or [quote form](/#quote).
- Never invent prices, stock, lead times, or shipping terms. For those, point to the [quote form](/#quote) or phone 555-666-7777.
- Never say the reseller is an authorized or official ELAFLEX distributor. It is independent.
- Safety: if someone describes a leak or uncontrolled gas release, tell them to release the lever, use the emergency stop, clear the area and call emergency services if needed, before anything else.
- Don't give installation or repair instructions beyond what the knowledge base says; recommend a qualified LP-gas technician and the authority having jurisdiction for code questions.
- Off-topic questions: politely say you only cover the GG20 and related GasGuard products.
- If the visitor wants to buy or gives contact details, thank them and point to the [quote form](/#quote).

KNOWLEDGE BASE (excerpts):
`;

export async function onRequestPost({ request, env }) {
  if (!env.GROQ_API_KEY) return json({ reply: "Chat isn't configured yet. Please use the [quote form](/#quote) or call 555-666-7777." });
  let body;
  try { body = await request.json(); } catch { return json({ error: "bad_request" }, 400); }

  const messages = (Array.isArray(body.messages) ? body.messages : [])
    .slice(-6)
    .filter((m) => (m.role === "user" || m.role === "assistant") && typeof m.content === "string")
    .map((m) => ({ role: m.role, content: m.content.slice(0, 800) }));
  while (messages.length && messages[0].role !== "user") messages.shift();
  if (!messages.length || messages[messages.length - 1].role !== "user") return json({ error: "no_question" }, 400);

  // Retrieve on the last two user turns so follow-ups ("what about the DN?") keep their context.
  const query = messages.filter((m) => m.role === "user").slice(-2).map((m) => m.content).join(" ");
  const model = env.CHAT_MODEL || "openai/gpt-oss-20b";
  // Reasoning options only exist on reasoning models; other Groq models reject them.
  const reasoning = /gpt-oss/.test(model) ? { reasoning_effort: "low", include_reasoning: false } : {};
  const r = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: { authorization: `Bearer ${env.GROQ_API_KEY}`, "content-type": "application/json" },
    body: JSON.stringify({
      model,
      max_completion_tokens: 500, // includes the model's hidden reasoning
      ...reasoning,
      temperature: 0.2,
      messages: [{ role: "system", content: rules + relevantKB(query) }, ...messages],
    }),
  });
  if (r.status === 429 || r.status === 413) return json({ reply: "The chat is busy right now. Please try again in a minute, call 555-666-7777, or use the [quote form](/#quote)." });
  if (!r.ok) { console.error("groq", r.status, await r.text()); return json({ error: "upstream" }, 502); }
  const out = await r.json();
  const reply = (out.choices?.[0]?.message?.content || "").trim()
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
