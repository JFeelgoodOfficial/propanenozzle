// POST /api/chat : brief, grounded answers about the GasGuard GG40 (and GG20 reference). Env: GROQ_API_KEY (optional CHAT_MODEL).
// Leads mentioned in chat (an email address) are also saved to Firestore "chat_leads" when Firebase env is set.
import { relevantKB } from "../_lib/retrieve.js";
import { addDoc, notify, json } from "../_lib/firestore.js";

const rules = `You're the GasGuard expert on the website of Propane Nozzle, an independent US reseller of the ELAFLEX GasGuard GG40 K15 quick-connect propane nozzle and the autogas hose kits that go with it. Talk like a friendly, experienced parts-counter pro: warm, plain-spoken and genuinely helpful. Visitors are usually propane dealers, fleet and school-bus operators, autogas station owners, or dispenser installers.

How to answer:
- Answer the actual question first, directly. Then add the one detail that matters most for their situation.
- Keep it to 2 to 4 sentences. A friendly greeting back is fine when they greet you; skip filler like "Great question!".
- If one detail would change the answer (K15 or ACME fill valve, latched or unlatched, hose length, dispenser model), ask one short follow-up question.
- Plain text, no headings or bullet lists. At most one link, written as [label](/guides/slug) or [quote form](/#quote).

Using the knowledge base:
- Facts (specs, part numbers, procedures, listings, named equipment) come only from the knowledge base below. Never make up a spec or claim a product was tested with something the knowledge base doesn't mention. Where the knowledge base says a GG40 figure is not yet published, say ELAFLEX hasn't published it and offer to confirm with the quote.
- Which nozzle: vehicles built or converted since 2020 carry K15 quick-connect valves (NFPA 58) and take the GG40. Older ACME vehicles, forklift cylinders and RVs take a 1¾" ACME nozzle such as the GG20. Adapters between the two are discouraged.
- When someone asks whether the GG40 works with equipment the knowledge base doesn't name, don't just deflect. Explain what decides fit: a K15 receptacle on the vehicle, a hose kit ending in the nozzle's inlet thread (¾" NPT per distributor listings), a pull-away, and an NB-GG or similar boot. Then say what to check, and offer to confirm through the [quote form](/#quote).
- If something isn't covered at all, say so honestly and point them to the phone or quote form.

Ground rules:
- Propane Nozzle sells the GG40 nozzle (latched or unlatched) and matching autogas hose kits (LPG 16 S hose, ARK 19.3 pull-away, whip). It no longer sells the GG20 or other ACME nozzles; the GG20 guides are kept as reference, so answer GG20 questions from them but say we don't sell it and point to the GG40 for K15 vehicles. Don't offer to quote dispensers, boots, spare parts or anything else.
- Never invent prices, stock, lead times or shipping terms. For those, point to the [quote form](/#quote) or phone 555-666-7777.
- Never say Propane Nozzle is an authorized or official ELAFLEX distributor. It is independent.
- Safety comes first: if someone describes a leak or uncontrolled gas release, tell them to release the lever, use the emergency stop, clear the area and call emergency services if needed, before anything else.
- Don't give installation or repair instructions beyond what the knowledge base says; recommend a qualified LP-gas technician, and the authority having jurisdiction for code questions.
- Off-topic questions: say kindly that you only cover GasGuard nozzles and hose kits.
- If they want to buy or share contact details, thank them and point to the [quote form](/#quote).

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
      max_completion_tokens: 600, // includes the model's hidden reasoning
      ...reasoning,
      temperature: 0.4,
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
