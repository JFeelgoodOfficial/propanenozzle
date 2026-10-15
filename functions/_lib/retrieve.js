// Picks the knowledge-base sections most relevant to a question, so each chat request
// stays well under Groq's free-tier tokens-per-minute limit instead of sending the whole KB.
import { KB } from "./kb.js";

const STOP = new Set(("a an and are as at be but by can do does for from has have how i if in is it its me my of on or " +
  "so than that the their them then there these they this to was we what when where which who why will with you your " +
  "about any get need want use using would could should just like also not no yes come comes").split(" "));
// Crude stemmer, applied to both questions and KB: leaking/leaks -> leak, rate/rated/ratings -> rat.
const stem = (w) => (w.length > 3 && !/\d/.test(w) ? w.replace(/(ings|ing|ed|es|s)$/, "").replace(/(.{3,})e$/, "$1") : w);
// Hyphenated words count whole and as parts, so "self service" matches "self-service" and "p4-150" still matches exactly.
const words = (s) => (s.toLowerCase().match(/[a-z0-9]+(?:[.\-/][a-z0-9]+)*/g) || [])
  .flatMap((w) => (w.includes("-") ? [w, ...w.split("-")] : [w]))
  .filter((w) => w.length > 1 && !STOP.has(w)).map(stem);

// The KB is "# Guide title\nURL: ...\n\nSummary...\n## Section\n...". Header block first, then one guide per "# ".
const [HEADER, ...GUIDES] = KB.split(/\n(?=# )/);
const CHUNKS = [];
GUIDES.forEach((g, gi) => {
  const [intro, ...sections] = g.trim().split(/\n(?=## )/);
  const lines = intro.split("\n");
  const head = lines.slice(0, 2).join("\n"); // "# Title" + "URL: ..."
  const title = lines[0];
  CHUNKS.push({ text: intro, title, body: intro, guide: gi, intro: true });
  for (const s of sections) CHUNKS.push({ text: head + "\n" + s, title: title + " " + s.split("\n")[0], body: s.trim(), guide: gi });
});
// BM25 over sections, so a short section that answers the question beats a long one that merely mentions its words.
const DOCS = CHUNKS.map((c) => {
  const toks = words(c.text), tf = new Map();
  for (const t of toks) tf.set(t, (tf.get(t) || 0) + 1);
  return { ...c, tf, len: toks.length, titleTerms: new Set(words(c.title)) };
});
const DF = new Map();
for (const d of DOCS) for (const t of d.tf.keys()) DF.set(t, (DF.get(t) || 0) + 1);
const N = DOCS.length, AVG = DOCS.reduce((a, d) => a + d.len, 0) / N, K1 = 1.2, B = 0.75;
const idf = (t) => Math.log(1 + (N - DF.get(t) + 0.5) / (DF.get(t) + 0.5));
const bm25 = (d, t) => { const f = d.tf.get(t) || 0; return f ? idf(t) * (f * (K1 + 1)) / (f + K1 * (1 - B + B * d.len / AVG)) : 0; };

/** Returns the KB header plus the best-matching sections, in KB order, within `budget` characters. */
export function relevantKB(query, budget = 6000) {
  const q = [...new Set(words(query))].filter((t) => DF.has(t));
  const scored = DOCS.map((d, i) => ({
    i, d,
    score: q.reduce((s, t) => s + bm25(d, t) + (d.titleTerms.has(t) ? idf(t) : 0), 0),
  })).filter((x) => x.score > 0).sort((a, b) => b.score - a.score);

  const picked = [];
  const seen = new Set(); // guides that share a section word for word (e.g. the Parafour ordering table) count once
  let used = HEADER.length;
  // Each guide opens with a summary that carries its key numbers; always include the summaries of the two best guides.
  const topGuides = [...new Set(scored.map((x) => x.d.guide))].slice(0, 2);
  const intros = DOCS.map((d, i) => ({ i, d })).filter((x) => x.d.intro && topGuides.includes(x.d.guide));
  for (const x of [...intros, ...scored]) {
    if (seen.has(x.d.body) || used + x.d.text.length > budget) continue;
    seen.add(x.d.body); picked.push(x); used += x.d.text.length;
  }
  if (!picked.length) picked.push({ i: 0, d: DOCS[0] }); // greetings etc.: the model-comparison summary
  picked.sort((a, b) => a.i - b.i);
  return [HEADER.trim(), ...picked.map((x) => x.d.text.trim())].join("\n\n");
}
