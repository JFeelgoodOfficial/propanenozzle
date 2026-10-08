/* GG20 product Q&A widget. Talks to /api/chat. No cookies, no storage; history lives only in this page view. */
(function () {
  if (window.__gg20chat) return; window.__gg20chat = true;
  var css = `
  .gc-btn{position:fixed;right:16px;bottom:16px;z-index:40;background:#e8650f;color:#fff;border:0;border-radius:999px;padding:12px 18px;font:600 15px/1 "IBM Plex Sans",system-ui,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.18);cursor:pointer}
  @media (max-width:720px){.gc-btn{bottom:76px}}
  .gc-panel{position:fixed;right:16px;bottom:76px;z-index:41;width:min(380px,calc(100vw - 32px));height:min(540px,calc(100vh - 110px));background:var(--surface,#fff);color:var(--ink,#15191f);border:1px solid var(--line,#dcd9d2);border-radius:14px;box-shadow:0 18px 50px rgba(0,0,0,.22);display:none;flex-direction:column;overflow:hidden;font:15px/1.5 "IBM Plex Sans",system-ui,sans-serif}
  @media (max-width:720px){.gc-panel{bottom:130px;height:calc(100vh - 160px)}}
  .gc-panel.open{display:flex}
  .gc-head{background:#14213a;color:#f3f1ec;padding:12px 14px;display:flex;justify-content:space-between;align-items:center}
  .gc-head small{display:block;color:#b7bfcc;font-size:12px}
  .gc-x{background:none;border:0;color:#f3f1ec;font-size:22px;cursor:pointer;line-height:1}
  .gc-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
  .gc-m{max-width:88%;padding:9px 12px;border-radius:12px;white-space:pre-wrap;word-wrap:break-word}
  .gc-u{align-self:flex-end;background:#e8650f;color:#fff;border-bottom-right-radius:4px}
  .gc-a{align-self:flex-start;background:var(--chip,#eeece6);border-bottom-left-radius:4px}
  .gc-a a{color:var(--orange-ink,#b84c06)}
  .gc-sug{display:flex;flex-wrap:wrap;gap:6px}
  .gc-sug button{border:1px solid var(--line,#dcd9d2);background:transparent;color:inherit;border-radius:999px;padding:6px 10px;font:inherit;font-size:13px;cursor:pointer}
  .gc-form{display:flex;gap:8px;padding:10px;border-top:1px solid var(--line,#dcd9d2)}
  .gc-form input{flex:1;padding:10px 12px;border:1.5px solid var(--line,#dcd9d2);border-radius:8px;background:var(--bg,#f6f5f2);color:inherit;font:inherit}
  .gc-form button{background:#e8650f;color:#fff;border:0;border-radius:8px;padding:0 14px;font-weight:600;cursor:pointer}
  .gc-foot{font-size:11px;color:var(--muted,#5b6370);padding:0 12px 8px}`;
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var btn = el("button", "gc-btn", "Ask about the GG20");
  btn.setAttribute("aria-expanded", "false");
  var panel = el("div", "gc-panel"); panel.setAttribute("role", "dialog"); panel.setAttribute("aria-label", "GG20 product questions");
  panel.innerHTML = '<div class="gc-head"><div><strong>GG20 questions</strong><small>Answers from ELAFLEX documentation</small></div><button class="gc-x" aria-label="Close">×</button></div><div class="gc-log" aria-live="polite"></div><form class="gc-form"><input maxlength="500" placeholder="e.g. Will it fit a forklift cylinder?" aria-label="Your question" required><button type="submit">Send</button></form><div class="gc-foot">Automated answers can be wrong. For safety-critical decisions, check the ELAFLEX manual or call us.</div>';
  document.body.appendChild(btn); document.body.appendChild(panel);
  var log = panel.querySelector(".gc-log"), form = panel.querySelector("form"), input = form.querySelector("input");
  var history = [], busy = false;

  say("a", "Hi. Ask anything about the ELAFLEX GasGuard GG20: which version to pick, specs, fitting, maintenance or ordering.");
  var sug = el("div", "gc-sug");
  ["GG20 vs GG20DN?", "Will it reach a forklift cylinder valve?", "Is the latch UL listed?", "How do I order?"].forEach(function (q) {
    var b = el("button", "", q); b.type = "button"; b.onclick = function () { sug.remove(); ask(q); }; sug.appendChild(b);
  });
  log.appendChild(sug);

  btn.onclick = function () { var o = panel.classList.toggle("open"); btn.setAttribute("aria-expanded", o); if (o) input.focus(); track("chat_open"); };
  panel.querySelector(".gc-x").onclick = function () { panel.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); };
  form.onsubmit = function (e) { e.preventDefault(); var q = input.value.trim(); if (q) { input.value = ""; ask(q); } };

  function ask(q) {
    if (busy) return; busy = true;
    say("u", q); history.push({ role: "user", content: q });
    var pending = say("a", "…");
    fetch("/api/chat", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: history.slice(-8), page: location.pathname }) })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (d) { render(pending, d.reply); history.push({ role: "assistant", content: d.reply }); track("chat_answer"); })
      .catch(function () { render(pending, "I can't answer right now. Call 555-666-7777, email sales@propanenozzle.com, or use the [quote form](/#quote)."); })
      .finally(function () { busy = false; });
  }
  function say(who, text) { var m = el("div", "gc-m gc-" + who); render(m, text); log.appendChild(m); log.scrollTop = log.scrollHeight; return m; }
  function render(node, text) {
    var safe = String(text).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
    // only allow [text](/path) or [text](https://...) links
    safe = safe.replace(/\[([^\]]{1,80})\]\(((?:\/|https:\/\/)[^\s)]{0,200})\)/g, function (_, t, u) {
      var ext = u.indexOf("https://") === 0 && u.indexOf(location.host) === -1;
      return '<a href="' + u + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + ">" + t + "</a>";
    });
    node.innerHTML = safe; log.scrollTop = log.scrollHeight;
  }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text) n.textContent = text; return n; }
  function track(ev) { try { (window.dataLayer = window.dataLayer || []).push({ event: ev }); } catch (e) {} }
})();
