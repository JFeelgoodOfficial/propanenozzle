// Checks that the chat's knowledge-base retrieval finds the right section for common questions.
// Run after editing build/content.py or functions/_lib/retrieve.js:  node scripts/test-retrieval.mjs
import { relevantKB } from "../functions/_lib/retrieve.js";

// question -> text that must appear in what the chat model is given
const CASES = {
  "does the GG20H come with a latch": "Can I get a GG20H or GG20DN with a latch",
  "can I get a GG20DN with a magnet": "Can I get a GG20H or GG20DN with a latch",
  "what part number is the GG20DN nose piece": "Nose pieces on the GG20, GG20H and GG20DN",
  "how do I replace the nose piece on a GG20DN": "Nose pieces on the GG20, GG20H and GG20DN",
  "what is the lever force of the GG20H": "How much lever force",
  "GG20 splashguard option": "Option suffixes",
  "GG20DN.3 part number": "Catalogue part numbers",
  "what does .3 mean": "½\" NPT female",
  "what does the B option mean": "brass",
  "seal kit for GG20DN": "GG3",
  "What is the flow rate of the GG20?": "63 L/min",
  "whats the burst pressure": "1450",
  "what temperature range can it handle": "−40 °C",
  "how heavy is it": "2.0 kg",
  "does it have a strainer": "300 µm",
  "is it UL listed": "UL 125",
  "difference between GG20H and GG20DN": "GG20DN: when you can't control who fills",
  "is the gg20dn good for self service": "self-service",
  "my nozzle is leaking when I disconnect": "Troubleshooting",
  "lever is stiff": "Stiff Lever",
  "how often should I inspect it": "6 to 12",
  "can I use teflon tape": "PTFE",
  "How do I replace my LG20?": "Replacing a GasGuard LG20",
  "does it fit a forklift cylinder": "Forklift",
  "NFPA 58 rules": "NFPA 58",
  "california rule 1177": "1177",
  "what nozzle for K15 vehicles": "GG40",
  "will a gg20 work with a p4-150": "GG20 on the Parafour P4-150",
  "will a gg20 work with a p4-200": "GG20 on the Parafour P4-200",
  "p4-075": "P4-075",
  "does it work with my parafour dispenser": "Parafour",
  "hi": "GG20 vs GG20H",
};

let failed = 0;
for (const [q, want] of Object.entries(CASES)) {
  const kb = relevantKB(q);
  const ok = kb.includes(want);
  if (!ok) failed++;
  console.log(`${ok ? "PASS" : "FAIL"}  ~${Math.round(kb.length / 4)} tok  ${q}`);
}
console.log(`\n${Object.keys(CASES).length - failed}/${Object.keys(CASES).length} passed`);
process.exit(failed ? 1 : 0);
