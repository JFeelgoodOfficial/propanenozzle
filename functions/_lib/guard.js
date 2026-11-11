// Browsers send an Origin header on every POST made by fetch(). Requiring it to match the host the request
// arrived on keeps other sites and simple scripts from spending the chat quota or filling the lead list.
// It works unchanged on the live domain and on Cloudflare preview URLs. It is a filter, not authentication.
export function sameOrigin(request) {
  const origin = request.headers.get("origin");
  if (!origin) return false;
  try { return new URL(origin).host === new URL(request.url).host; } catch { return false; }
}
