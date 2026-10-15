// Light/dark toggle. Cycles Auto (follows the device setting) -> Light -> Dark.
// The early <head> snippet applies a saved choice before first paint; this file wires up the button.
(function () {
  var root = document.documentElement;
  var ORDER = ["auto", "light", "dark"];
  var LABEL = { auto: "Auto", light: "Light", dark: "Dark" };
  var ICON = {
    auto: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 4a8 8 0 0 1 0 16z" fill="currentColor"/></svg>',
    light: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></g></svg>',
    dark: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg>'
  };

  function saved() {
    try { var t = localStorage.getItem("theme"); return t === "light" || t === "dark" ? t : "auto"; } catch (e) { return "auto"; }
  }
  function apply(mode) {
    if (mode === "auto") root.removeAttribute("data-theme"); else root.setAttribute("data-theme", mode);
    try { if (mode === "auto") localStorage.removeItem("theme"); else localStorage.setItem("theme", mode); } catch (e) {}
  }
  function render(btn, mode) {
    var next = ORDER[(ORDER.indexOf(mode) + 1) % ORDER.length];
    btn.innerHTML = ICON[mode] + "<span>" + LABEL[mode] + "</span>";
    btn.setAttribute("aria-label", "Theme: " + LABEL[mode] + (mode === "auto" ? " (follows your device)" : "") + ". Switch to " + LABEL[next] + ".");
    btn.title = btn.getAttribute("aria-label");
  }

  function init() {
    var btns = document.querySelectorAll("[data-theme-toggle]");
    var mode = saved();
    btns.forEach(function (btn) {
      render(btn, mode);
      btn.addEventListener("click", function () {
        mode = ORDER[(ORDER.indexOf(mode) + 1) % ORDER.length];
        apply(mode);
        btns.forEach(function (b) { render(b, mode); });
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
