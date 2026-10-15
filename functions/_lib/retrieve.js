// Picks the knowledge-base sections most relevant to a question, so each chat request
// stays well under Groq's free-tier tokens-per-minute limit instead of sending the whole KB.
import { KB } from "./kb.js";

const STOP = new Set(("a an and are as at be but by can do does for from has have how i if in is it its me my of on or " +
  "so than that the their them then there these they this to was we what when where which who why will with you your " +
  "about any get need want use using would could should just like also not no yes").split(" "));
const stem = (w) => (w.length > 4 && !/\d/.test(w) ? w.replace(/(ing|ed|es|s)$/, "") : w); // leaking, leaks -> leak
const words = (s) => (s.toLowerCase().match(/[a-z0-9]+(?:[.\-/][a-z0-9]+)*/g) || []).filter((w) => w.length > 1 && !STOP.has(w)).map(stem);

// The KB is "# Guide title\nURL: ...\n\nSummary...\n## Section\n...". Header block first, then one guide per "# ".
const [HEADER, ...GUIDES] = KB.split(/\n(?=# )/);
const CHUNKS = [];
for (const g of GUIDES) {
  const [intro, ...sections] = g.trim().split(/\n(?=## )/);
  const lines = intro.split("\n");
  const head = lines.slice(0, 2).join("\n"); // "# Title" + "URL: ..."
  const title = lines[0];
  CHUNKS.push({ text: intro, title });
  for (const s of sections) CHUNKS.push({ text: head + "\n" + s, title: title + " " + s.split("\n")[0] });
}
const DOCS = CHUNKS.map((c) => ({ ...c, terms: new Set(words(c.text)), titleTerms: new Set(words(c.title)) }));
const DF = new Map();
for (const d of DOCS) for (const t of d.terms) DF.set(t, (DF.get(t) || 0) + 1);
const idf = (t) => Math.log(1 + DOCS.length / (DF.get(t) || DOCS.length));

/** Returns the KB header plus the best-matching sections, in KB order, within `budget` characters. */
export function relevantKB(query, budget = 6000) {
  const q = [...new Set(words(query))].filter((t) => DF.has(t));
  const scored = DOCS.map((d, i) => ({
    i, d,
    score: q.reduce((s, t) => s + (d.terms.has(t) ? idf(t) : 0) + (d.titleTerms.has(t) ? idf(t) : 0), 0),
  })).filter((x) => x.score > 0).sort((a, b) => b.score - a.score);

  const picked = [];
  let used = HEADER.length;
  for (const x of scored) {
    if (used + x.d.text.length > budget) continue;
    picked.push(x); used += x.d.text.length;
  }
  if (!picked.length) picked.push({ i: 0, d: DOCS[0] }); // greetings etc.: the model-comparison summary
  picked.sort((a, b) => a.i - b.i);
  return [HEADER.trim(), ...picked.map((x) => x.d.text.trim())].join("\n\n");
}
