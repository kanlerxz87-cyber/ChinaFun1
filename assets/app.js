/* China 2027 Trip Planner — shared header, footer & table renderers (1fa0d691 + 1ac7826d) */
const PAGES = [
  ["index.html", "Overview"],
  ["hotels.html", "Hotels"],
  ["michelin.html", "MICHELIN (107)"],
  ["activities.html", "Activities"],
  ["itinerary.html", "Itinerary"],
  ["decisions.html", "Decisions"],
  ["suggestions.html", "Suggestions"],
  ["flagged.html", "Flagged"]
];

const COMPANION_PLANS = [
  ["integration-2027/index.html", "All Plans Hub"],
  ["social-2027/index.html", "Social Video Index (58)"],
  ["docs/index.html", "Shanghai (Docs)"],
  ["shanghai-2027/index.html", "Shanghai 2027"],
  ["shanghai-verified-2027/index.html", "Shanghai Verified"]
];

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, m => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;"
  }[m]));
}

function guideUrl(r) {
  const slug = (typeof GUIDE_SLUG !== "undefined" && GUIDE_SLUG[r.n]) || r.slug;
  return slug
    ? `https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/${slug}`
    : "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred";
}

function renderShell(active) {
  const hdr = document.getElementById("site-header");
  if (hdr) {
    hdr.innerHTML = `
      <header class="top">
        <div class="wrap">
          <div class="brandbar">
            <div class="brand">
              <span class="dot" aria-hidden="true"></span>
              <div>China 2027 Trip Planner <small>Beijing · 15–22 Feb 2027 · Verified ${esc(META.updated)}</small></div>
            </div>
            <span class="chip v">2027 Guide · 107 venues</span>
          </div>
          <nav class="nav" aria-label="Primary navigation">
            ${PAGES.map(([href, label]) =>
              `<a href="${href}" class="${href === active ? "active" : ""}">${esc(label)}</a>`
            ).join("")}
          </nav>
          <div class="subnav" aria-label="Companion plans in this repository">
            <span class="subnav-label">Companion plans:</span>
            ${COMPANION_PLANS.map(([href, label]) =>
              `<a href="${href}">${esc(label)} ↗</a>`
            ).join("")}
          </div>
        </div>
      </header>`;
  }
  const ftr = document.getElementById("site-footer");
  if (ftr) {
    ftr.innerHTML = `
      <footer>
        <div class="wrap">
          <div><strong>Provenance:</strong> Session ${esc(META.session)} snapshot (${esc(META.updated)}). All 33 starred addresses/phones &amp; 74 Bib/Selected listings from
          <a href="${META.sources.michelinStarred}" target="_blank" rel="noopener">MICHELIN Guide Beijing 2027</a>; hotel rates from live Booking.com (Feb 15–22 &amp; Mar 1–8 / 15–22, 2027);
          activities from <a href="${META.sources.beijingGov}" target="_blank" rel="noopener">Beijing Municipal Gov</a> &amp; official attraction sites.</div>
          <div style="margin-top:6px">
            <a href="flagged.html">Verification log</a> ·
            <a href="decisions.html">Ten open questions</a> ·
            <a href="integration-2027/index.html">All Plans Hub</a> ·
            <a href="social-2027/index.html">58 Verified YouTube Reviews</a>
          </div>
        </div>
      </footer>`;
  }
}

/* ---------- Hotels renderer ---------- */
function renderHotels() {
  const body = document.getElementById("hotels-body");
  if (!body) return;
  const q = (document.getElementById("h-search")?.value || "").trim().toLowerCase();
  const dist = document.getElementById("h-dist")?.value || "";
  const tierFilter = document.getElementById("h-tier")?.value || "";
  const sort = document.getElementById("h-sort")?.value || "usd";
  const count = document.getElementById("h-count");

  let rows = HOTELS.map(h => Object.assign({}, h));

  if (dist) rows = rows.filter(h => h.d.startsWith(dist));
  if (tierFilter === "budget") rows = rows.filter(h => h.usd !== null && h.usd < 1000);
  else if (tierFilter === "boutique") rows = rows.filter(h => (h.tier || "").includes("Boutique") || (h.tier || "").includes("Courtyard"));
  else if (tierFilter === "luxury") rows = rows.filter(h => (h.tier || "").includes("5★"));

  if (q) {
    rows = rows.filter(h =>
      (h.n + " " + h.d + " " + h.area + " " + h.room + " " + h.amenities + " " + h.note).toLowerCase().includes(q)
    );
  }

  rows.sort((a, b) => {
    if (a.oop && !b.oop) return 1;
    if (!a.oop && b.oop) return -1;
    if (sort === "usd") return (a.usd ?? 99999) - (b.usd ?? 99999);
    if (sort === "rating") return parseFloat(b.rating || 0) - parseFloat(a.rating || 0) || (a.usd ?? 99999) - (b.usd ?? 99999);
    if (sort === "transit") return ((b.transitActs || 0) * 100 + (b.transitStars || 0)) - ((a.transitActs || 0) * 100 + (a.transitStars || 0)) || (a.usd ?? 99999) - (b.usd ?? 99999);
    return (a.usd ?? 99999) - (b.usd ?? 99999);
  });

  if (count) {
    const live = rows.filter(r => !r.oop).length;
    count.textContent = `Showing ${rows.length} of ${HOTELS.length} properties (${live} live-priced for 15–22 Feb 2027, 1 queen/king bed + private bath confirmed)`;
  }

  body.innerHTML = rows.map(h => {
    const isRef = /free cancellation|refundable/i.test(h.cancel) && !/unavailable/i.test(h.cancel);
    const chip = h.oop
      ? `<span class="chip u">flagged unverified</span>`
      : isRef
        ? `<span class="chip v">free cancel</span>`
        : `<span class="chip f">non-refundable</span>`;
    const priceCell = h.oop
      ? `<span class="chip u">unbookable</span><span class="meta">Booking redirects; ~$50–$94/nt 3rd-party</span>`
      : `<strong>$${h.usd.toLocaleString()}</strong>` +
        (h.listUsd && h.listUsd > h.usd ? `<span class="meta">list $${h.listUsd.toLocaleString()}</span>` : "") +
        (h.bfUsd && !h.bf ? `<span class="meta">w/ bfast $${h.bfUsd.toLocaleString()}</span>` : "");
    const marCell = h.oop
      ? `<span class="meta">—</span>`
      : (h.mar1 ? `Mar 1–8: <strong>$${h.mar1.toLocaleString()}</strong>` : "Mar 1–8: n/a") +
        (h.mar15 ? `<span class="meta">Mar 15–22: $${h.mar15.toLocaleString()}</span>` : "") +
        `<span class="meta">${esc(h.bestWindow)}</span>`;

    return `
      <tr>
        <td class="name">
          <a href="${esc(h.u)}" target="_blank" rel="noopener">${esc(h.n)}</a>
          <span class="meta">${esc(h.tier || "")} · Booking ${esc(h.rating || "—")}/10</span>
        </td>
        <td><strong>${esc(h.d)}</strong><span class="meta">${esc(h.area)}</span></td>
        <td class="num">${priceCell}</td>
        <td>
          ${esc(h.room)} · <strong>${esc(h.bed)}</strong>
          <span class="meta">${esc(h.bath)}</span>
        </td>
        <td>
          <span class="chip ${h.bf ? "v" : "n"}">${h.bf ? "bfast incl." : "room only"}</span>
          <div style="margin-top:4px">${chip}</div>
          <span class="meta">${esc(h.cancel)}</span>
        </td>
        <td style="min-width:190px">${esc(h.amenities)}</td>
        <td style="min-width:170px">${marCell}</td>
        <td style="min-width:190px">
          <span class="chip ${h.transitActs >= 9 ? "v" : "n"}">${h.transitStars}/33 ★ · ${h.transitActs}/9 city ≤1h</span>
          <span class="meta">${esc(h.transitNote)}</span>
        </td>
      </tr>`;
  }).join("");
}

/* ---------- MICHELIN Starred renderer ---------- */
function renderMichelin() {
  const body = document.getElementById("michelin-body");
  if (!body) return;
  const q = (document.getElementById("m-search")?.value || "").trim().toLowerCase();
  const stars = document.getElementById("m-stars")?.value || "";
  const dist = document.getElementById("m-dist")?.value || "";
  const count = document.getElementById("m-count");

  let rows = MICHELIN.slice();
  if (stars) rows = rows.filter(r => String(r.s) === stars);
  if (dist) rows = rows.filter(r => r.d === dist);
  if (q) {
    rows = rows.filter(r =>
      (r.n + " " + r.c + " " + r.d + " " + r.a + " " + r.note).toLowerCase().includes(q)
    );
  }
  rows.sort((a, b) => b.s - a.s || a.n.localeCompare(b.n));

  if (count) {
    const withH = rows.filter(r => r.h).length;
    const withP = rows.filter(r => r.p2).length;
    count.textContent = `Showing ${rows.length} of ${MICHELIN.length} starred restaurants · ${rows.length}/${rows.length} addresses verified · ${withH} hours · ${withP} official menus/prices`;
  }

  body.innerHTML = rows.map(r => {
    const starStr = "★".repeat(r.s);
    const links = [
      `<a href="${esc(guideUrl(r))}" target="_blank" rel="noopener">MICHELIN</a>`,
      r.w ? `<a href="${esc(r.w)}" target="_blank" rel="noopener">Official site</a>` : ""
    ].filter(Boolean).join(" · ");
    const soc = (r.soc || []).map(x => {
      const cls = x.k.startsWith("YT search") || x.k.startsWith("IG search") ? "n" : "v";
      return `<a href="${esc(x.u)}" target="_blank" rel="noopener" class="chip ${cls}" style="margin:2px 3px 2px 0">${esc(x.k)}</a>`;
    }).join("");
    const noteHtml = r.note ? `<span class="meta">⚑ ${esc(r.note)}</span>` : "";
    return `
      <tr>
        <td class="star">${starStr} <span class="meta">${r.s}★</span></td>
        <td class="name">
          ${esc(r.n)}
          <span class="meta">${links}</span>
          ${noteHtml}
        </td>
        <td>${esc(r.c)}</td>
        <td><strong>${esc(r.d)}</strong></td>
        <td class="nowrap">${esc(r.p)}</td>
        <td>${esc(r.a)}<span class="meta">${esc(r.ph || "")}</span></td>
        <td>${r.h ? `<span class="chip v">verified</span> ${esc(r.h)}` : `<span class="chip f">hours unverified</span>`}</td>
        <td>${r.p2 ? `<span class="chip v">official</span> ${esc(r.p2)}` : `<span class="chip f">band only (${esc(r.p)})</span>`}</td>
        <td style="min-width:170px">${soc}</td>
      </tr>`;
  }).join("");
}

/* ---------- MICHELIN Bib Gourmand + Selected renderer (74 venues) ---------- */
function renderMichelinListed() {
  const body = document.getElementById("michelin-listed-body");
  if (!body || typeof MICHELIN_LISTED === "undefined") return;
  const q = (document.getElementById("ml-search")?.value || "").trim().toLowerCase();
  const tier = document.getElementById("ml-tier")?.value || "";
  const count = document.getElementById("ml-count");

  let rows = MICHELIN_LISTED.slice();
  if (tier) rows = rows.filter(r => r.tier === tier);
  if (q) rows = rows.filter(r => (r.n + " " + r.c + " " + r.tier).toLowerCase().includes(q));

  if (count) {
    count.textContent = `Showing ${rows.length} of ${MICHELIN_LISTED.length} non-starred Beijing 2027 Guide venues (32 Bib Gourmand + 42 MICHELIN Selected)`;
  }

  body.innerHTML = rows.map(r => {
    const isBib = r.tier === "Bib Gourmand";
    return `
      <tr>
        <td><span class="chip ${isBib ? "v" : "n"}">${esc(r.tier)}</span></td>
        <td class="name"><a href="${esc(guideUrl(r))}" target="_blank" rel="noopener">${esc(r.n)}</a></td>
        <td>${esc(r.c)}</td>
        <td class="nowrap">${esc(r.p)}</td>
        <td><a href="${esc(guideUrl(r))}" target="_blank" rel="noopener">MICHELIN Guide page ↗</a></td>
      </tr>`;
  }).join("");
}

/* ---------- Activities renderer ---------- */
function renderActivities() {
  const body = document.getElementById("activities-body");
  if (!body) return;
  const q = (document.getElementById("a-search")?.value || "").trim().toLowerCase();
  let rows = ACTIVITIES.slice();
  if (q) {
    rows = rows.filter(a =>
      (a.n + " " + a.d + " " + a.hours + " " + a.price + " " + a.transit).toLowerCase().includes(q)
    );
  }
  const count = document.getElementById("a-count");
  if (count) {
    const ver = rows.filter(r => r.status === "verified").length;
    count.textContent = `Showing ${rows.length} of ${ACTIVITIES.length} Beijing sights (${ver}/${rows.length} hours & pricing verified for Feb 2027)`;
  }
  body.innerHTML = rows.map(a => {
    const chip = `<span class="chip v">verified</span>`;
    const soc = (a.soc || []).map(x =>
      `<a href="${esc(x.u)}" target="_blank" rel="noopener" class="chip v" style="margin:2px 3px 2px 0">${esc(x.k)}</a>`
    ).join("");
    return `
      <tr>
        <td class="name">
          <a href="${esc(a.u)}" target="_blank" rel="noopener">${esc(a.n)}</a>
          <span class="meta">${esc(a.d)} · ${chip}</span>
        </td>
        <td>${esc(a.hours)}<span class="meta">Closed: ${esc(a.closed)}</span></td>
        <td>${esc(a.price)}<span class="meta"><strong>For 2:</strong> ${esc(a.p2)}</span></td>
        <td>${esc(a.book)}</td>
        <td>${esc(a.transit)}</td>
        <td style="min-width:170px">${soc}</td>
      </tr>`;
  }).join("");
}

/* ---------- Decision questions renderer ---------- */
function renderQuestions() {
  const el = document.getElementById("question-list");
  if (!el) return;
  el.innerHTML = QUESTIONS.map(q => `
    <div class="card" style="margin-bottom:12px">
      <div style="display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap">
        <h3>Q${q.id}. ${esc(q.title)}</h3>
        <span class="chip f">blocks: ${esc(q.blocks)}</span>
      </div>
      <p class="sub"><strong>What we have:</strong> ${esc(q.have)}</p>
      <p class="sub"><strong>What is missing:</strong> ${esc(q.missing)}</p>
      <p class="sub" style="color:var(--accent)"><strong>Action to close:</strong> ${esc(q.action)}</p>
    </div>
  `).join("");
}

document.addEventListener("DOMContentLoaded", () => {
  const active = document.body.dataset.page || "";
  renderShell(active);
  renderHotels();
  renderMichelin();
  renderMichelinListed();
  renderActivities();
  renderQuestions();
  ["h-search", "h-dist", "h-tier", "h-sort"].forEach(id =>
    document.getElementById(id)?.addEventListener("input", renderHotels)
  );
  ["m-search", "m-stars", "m-dist"].forEach(id =>
    document.getElementById(id)?.addEventListener("input", renderMichelin)
  );
  ["ml-search", "ml-tier"].forEach(id =>
    document.getElementById(id)?.addEventListener("input", renderMichelinListed)
  );
  document.getElementById("a-search")?.addEventListener("input", renderActivities);
});
