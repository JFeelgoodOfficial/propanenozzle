/* Site analytics: Google Analytics 4 plus first-touch lead attribution. Generated from build/templates/analytics.js.
   Every page loads this file. Pages call window.pnTrack(eventName, params); nothing else talks to gtag directly.
   With no GA4 id in site.json the events still reach window.dataLayer, but nothing is sent to Google. */
(function () {
  if (window.pnTrack) return;
  var GA_ID = "G-2M0W1FT2GG";
  var w = window, d = document;
  w.dataLayer = w.dataLayer || [];
  w.gtag = w.gtag || function () { w.dataLayer.push(arguments); };

  // Content group: which part of the site a page belongs to, so GA can compare sales pages with reference pages.
  var meta = d.querySelector('meta[name="content-group"]');
  var group = meta ? meta.content : "other";

  if (GA_ID) {
    var s = d.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
    d.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", GA_ID, {
      content_group: group,
      // Lead-generation site: no advertising features. Turn these on in site.json only if you add Google Ads remarketing,
      // and update /privacy.html when you do.
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    });
  }

  w.pnTrack = function (name, params) {
    try { gtag("event", name, Object.assign({ content_group: group }, params || {})); } catch (e) {}
  };

  /* ---- First-touch attribution ----------------------------------------------------------------------------
     Remembers how this visitor first arrived (landing page, referrer, UTM tags, Google Ads click id) so the quote
     form can send it with the lead even if they wander through several guides before asking for a price.
     Stored in this browser only; if storage is blocked the form falls back to the current page. */
  var KEY = "pn_first_touch", ft = null;
  try { ft = JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) {}
  var q; try { q = new URLSearchParams(location.search); } catch (e) { q = { get: function () { return null; } }; }
  var tags = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"];
  var hasTags = tags.some(function (k) { return q.get(k); });
  var external = d.referrer && d.referrer.indexOf(location.host) === -1;
  if (!ft || hasTags) { // a tagged campaign link replaces an older untagged first touch
    ft = { landing_page: location.pathname, referrer: external ? d.referrer.slice(0, 300) : (ft && ft.referrer) || "", first_seen: new Date().toISOString().slice(0, 10) };
    tags.forEach(function (k) { if (q.get(k)) ft[k] = q.get(k).slice(0, 200); });
    try { localStorage.setItem(KEY, JSON.stringify(ft)); } catch (e) {}
  }
  var pages = 0; try { pages = +sessionStorage.getItem("pn_pages") + 1; sessionStorage.setItem("pn_pages", pages); } catch (e) {}

  // Fills any hidden attribution fields in a form. Called by the quote form just before it submits.
  w.pnAttribution = function (form) {
    var cid = "";
    var m = d.cookie.match(/(?:^|; )_ga=GA\d\.\d\.(\d+\.\d+)/); if (m) cid = m[1];
    var v = Object.assign({ ga_client_id: cid, pages_viewed: String(pages || "") }, ft || { landing_page: location.pathname });
    Object.keys(v).forEach(function (k) {
      var el = form.querySelector('input[name="' + k + '"]');
      if (!el) { el = d.createElement("input"); el.type = "hidden"; el.name = k; form.appendChild(el); }
      if (v[k]) el.value = v[k];
    });
  };

  /* ---- Site-wide clicks ---------------------------------------------------------------------------------- */
  function where(el) { var s = el.closest("section[id],header,footer,aside,nav,.mbar,.topbar"); return s ? (s.id || s.className || s.tagName).toString().split(" ")[0].toLowerCase() : "page"; }
  d.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a,button"); if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("mailto:") === 0) return w.pnTrack("contact_click", { method: "email", link_location: where(a) });
    if (href.indexOf("tel:") === 0) return w.pnTrack("contact_click", { method: "phone", link_location: where(a) });
    if (/#quote$/.test(href)) return w.pnTrack("quote_cta_click", { link_location: where(a), link_text: (a.textContent || "").trim().slice(0, 60) });
    if (a.hasAttribute("data-track")) return w.pnTrack("cta_click", { cta: a.getAttribute("data-track"), link_location: where(a) });
  }, true);

  // Which GG40 product page sections people actually reach, in order. Fires once per section per page view.
  if ("IntersectionObserver" in w) {
    d.addEventListener("DOMContentLoaded", function () {
      var seen = {}, secs = d.querySelectorAll("main section[id]");
      if (!secs.length) return;
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          var id = en.target.id;
          if (en.isIntersecting && !seen[id]) { seen[id] = 1; w.pnTrack("section_view", { section: id }); io.unobserve(en.target); }
        });
      }, { threshold: 0.35 });
      secs.forEach(function (s) { io.observe(s); });
    });
  }
})();
