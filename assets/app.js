/* Shared UI: nav, table renderers, filtering. No dependencies. */
(function(){
  const PAGES = [
    ["index.html","Beijing overview"],
    ["integration-2027/index.html","All plans"],
    ["hotels.html","Hotels"],
    ["michelin.html","MICHELIN"],
    ["activities.html","Activities"],
    ["social-2027/index.html","Social index"],
    ["itinerary.html","Itinerary"],
    ["decisions.html","Open questions"],
    ["suggestions.html","Suggestions"],
    ["flagged.html","Verification log"]
  ];

  function esc(s){ return String(s==null?"":s).replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }

  function header(active){
    const links = PAGES.map(([h,l])=>`<a href="${h}" class="${h===active?'active':''}">${l}</a>`).join("");
    return `<header class="top"><div class="wrap">
      <div class="brandbar">
        <div class="brand"><span class="dot"></span><span>China 2027<small>Beijing · 15 Feb – 22 Feb 2027</small></span></div>
        <span class="chip n">Verified ${META.updated}</span>
      </div>
      <nav class="nav">${links}</nav>
    </div></header>`;
  }
  function footer(){
    return `<footer><div class="wrap">
      <p><strong>Method:</strong> every value in this planner was read directly from the linked official or primary-verified source (initial snapshot 25 Nov 2026; full 33-restaurant, municipal activity &amp; social verification pass ${META.updated}).
      Values that could not be confirmed are left blank and flagged rather than estimated.</p>
      <p>Sources: MICHELIN Guide (guide.michelin.com / michelin.com), restaurant websites &amp; menu PDFs, Booking.com live rate pages (25 Nov 2026), Beijing Municipal Government (english.beijing.gov.cn), Palace Museum (intl.dpm.org.cn), Mutianyu Great Wall (en.mutianyugreatwall.com), National Museum of China (en.chnmuseum.cn), YouTube oEmbed / watch pages, U.S. State Department, timeanddate.com. Not affiliated with any listed business.</p>
      <p>Session ${META.session} · data file <code>assets/data.js</code> · see <a href="flagged.html">Verification log</a> for known gaps.</p>
    </div></footer>`;
  }

  function mount(){
    const page = document.body.dataset.page || "index.html";
    const h = document.getElementById("site-header");
    if(h) h.innerHTML = header(page);
    const f = document.getElementById("site-footer");
    if(f) f.innerHTML = footer();
    const y = document.getElementById("year"); if(y) y.textContent = "2027";

    if(document.getElementById("michelin-table")) renderMichelin();
    if(document.getElementById("bib-table")) renderNonStarred("bib-tbody", typeof BIB_GOURMAND!=="undefined"?BIB_GOURMAND:[], "Bib Gourmand");
    if(document.getElementById("selected-table")) renderNonStarred("selected-tbody", typeof MICHELIN_SELECTED!=="undefined"?MICHELIN_SELECTED:[], "MICHELIN Selected");
    if(document.getElementById("hotel-table")) renderHotels();
    if(document.getElementById("activity-table")) renderActivities();
    if(document.getElementById("question-list")) renderQuestions();
    wireFilters();
  }

  /* ---------- MICHELIN ---------- */
  function guideLink(r){
    const slug = (typeof GUIDE_SLUG!=="undefined" && GUIDE_SLUG[r.n]) ? GUIDE_SLUG[r.n] : null;
    const url = r.g || (slug ? `https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/${slug}` : "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred");
    return `<a href="${url}" target="_blank" rel="noopener">MICHELIN ↗</a>`;
  }
  function socialCell(r){
    if(!r.soc || !r.soc.length) return `<span class="chip u">none found</span>`;
    return r.soc.map(([l,u])=>`<a href="${u}" target="_blank" rel="noopener">${esc(l)}</a>`).join(" · ");
  }
  function renderMichelin(){
    const body = document.getElementById("michelin-tbody");
    const rows = MICHELIN.slice().sort((a,b)=> b.s-a.s || a.n.localeCompare(b.n));
    body.innerHTML = rows.map(r=>{
      const p2 = r.p2 ? esc(r.p2) : `<span class="chip u">not published</span>`;
      const hours = r.h ? esc(r.h) : `<span class="chip u">not published</span>`;
      const exc = r.closed ? `<div class="meta">Exceptions/closed: ${esc(r.closed)}</div>` : "";
      const fx = r.fx ? `<div class="srcline" style="margin-top:4px">⚑ ${esc(r.fx)}</div>` : "";
      return `<tr data-f="${esc((r.n+' '+r.c+' '+r.d+' '+r.a+' '+r.s+'-star').toLowerCase())}">
        <td class="name">${esc(r.n)}<span class="meta">${esc(r.c)}</span></td>
        <td><span class="star">${"★".repeat(r.s)}</span><span class="meta">${r.s}-star ${r.s===3?"Exceptional cuisine":r.s===2?"Excellent cooking":"High quality cooking"}</span></td>
        <td>${esc(r.p)}<span class="meta">MICHELIN price band</span></td>
        <td>${esc(r.d)||`<span class="chip u">blank</span>`}</td>
        <td>${esc(r.a)||`<span class="chip u">not captured</span>`}</td>
        <td>${hours}${exc}${fx}</td>
        <td>${r.ph?`<a href="tel:${esc(r.ph.replace(/[^+\d]/g,''))}">${esc(r.ph)}</a>`:"—"}</td>
        <td style="min-width:190px">${p2}</td>
        <td style="min-width:190px">${socialCell(r)}</td>
        <td class="nowrap">${guideLink(r)}${r.w?` · <a href="${r.w}" target="_blank" rel="noopener">site ↗</a>`:""}</td>
      </tr>`;
    }).join("");
    const c = document.getElementById("michelin-count");
    if(c) c.textContent = MICHELIN.length;
  }

  function renderNonStarred(tbodyId, items, tier){
    const body = document.getElementById(tbodyId);
    if(!body) return;
    body.innerHTML = items.map((item, idx)=>`
      <tr data-f="${esc((item.n+' '+item.c+' '+item.p+' '+tier).toLowerCase())}">
        <td class="num">${idx+1}</td>
        <td class="name">${esc(item.n)}</td>
        <td>${esc(item.c)}</td>
        <td>${esc(item.p)}</td>
        <td><span class="chip n">0★ · ${esc(tier)}</span></td>
        <td class="nowrap"><a href="https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/${esc(item.slug)}" target="_blank" rel="noopener">MICHELIN ↗</a></td>
      </tr>`).join("");
  }

  /* ---------- HOTELS ---------- */
  const W = {density:3, bed:3, review:2, cancel:1, price:3};
  function bedPts(b){ return b===true?W.bed : b==="partial"?W.bed/2 : 0; }
  function pricePts(night){ return night<=100?3 : night<=150?2 : night<=220?1 : 0; }
  function scoreHotel(h){
    const night = h.tot/7;
    const density = (DISTRICT_STARS[(h.area.split(" ")[0])]||0) * W.density;
    const bed = bedPts(h.bedOk);
    const rev = Math.max(0,(h.rev-8))*W.review;
    const cancel = h.cancel?W.cancel:0;
    const price = pricePts(night);
    return {night, density, bed, rev, cancel, price, total: density+bed+rev+cancel+price};
  }
  function renderHotels(){
    const body = document.getElementById("hotel-tbody");
    const scored = HOTELS.map(h=>({h, s:scoreHotel(h)}))
      .sort((a,b)=> (a.h.oop?1:0)-(b.h.oop?1:0) || b.s.total-a.s.total || a.h.tot-b.h.tot);
    let live = 0;
    body.innerHTML = scored.map((o)=>{
      const h=o.h, s=o.s;
      const pos = h.oop ? "—" : ++live;
      const bath = h.bath ? h.bath : "Bathroom unconfirmed — verify before booking";
      const bathShort = h.bath ? (h.bath.toLowerCase().includes("unconfirmed") ? "unconfirmed" : "private bath") : "unconfirmed";
      const bedCell = h.bedOk===true?`<span class="chip v">queen/king</span><span class="meta">${esc(bathShort)}</span>`
        : h.bedOk==="partial"?`<span class="chip f">request</span><span class="meta">${esc(bathShort)}</span>`
        : `<span class="chip u">twin only</span><span class="meta">${esc(bathShort)}</span>`;
      const f = esc((h.n+' '+h.area+' '+h.room+' '+h.bed).toLowerCase());
      return `<tr data-f="${f}">
        <td><span class="rank">${pos}</span></td>
        <td class="name">${esc(h.n)}${h.oop?' <span class="chip u">March only</span>':''}<span class="meta">${esc(h.area)} · Booking rating ${esc(h.cls)} · guest ${h.rev}/10</span></td>
        <td>${esc(h.room)}<span class="meta">${esc(h.bed)} · ${esc(bath)}</span></td>
        <td>${bedCell}</td>
        <td class="num">$${h.tot.toLocaleString()}<span class="meta">$${s.night.toFixed(0)}/night · 7 nights · 2 adults</span></td>
        <td class="num">${s.density}</td>
        <td class="num">${s.bed.toFixed(1)}</td>
        <td class="num">${s.rev.toFixed(1)}</td>
        <td class="num">${s.price}</td>
        <td class="num"><strong>${s.total.toFixed(1)}</strong></td>
        <td>${h.cancel?esc(h.cancel):"—"}</td>
        <td class="nowrap"><a href="${h.url}" target="_blank" rel="noopener">rate ↗</a></td>
      </tr>
      ${h.fx?`<tr data-f="${f}"><td></td><td colspan="11" class="srcline">⚑ ${esc(h.fx)}</td></tr>`:""}`;
    }).join("");
  }

  /* ---------- ACTIVITIES ---------- */
  function renderActivities(){
    const body = document.getElementById("activity-tbody");
    body.innerHTML = ACTIVITIES.map(a=>{
      const st = a.v?`<span class="chip v">verified</span>`:`<span class="chip u">unverified</span>`;
      return `<tr data-f="${esc((a.n+' '+a.area).toLowerCase())}">
        <td class="name">${esc(a.n)}<span class="meta">${esc(a.area)}</span></td>
        <td>${a.h?esc(a.h):`<span class="chip u">blank</span>`}</td>
        <td>${a.price?esc(a.price):`<span class="chip u">blank</span>`}</td>
        <td style="min-width:190px">${a.soc.length?a.soc.map(([l,u])=>`<a href="${u}" target="_blank" rel="noopener">${esc(l)}</a>`).join(" · "):`<span class="chip u">none found</span>`}</td>
        <td class="nowrap">${a.off?`<a href="${a.off}" target="_blank" rel="noopener">official ↗</a>`:""}${a.book?` · <a href="${a.book}" target="_blank" rel="noopener">tickets ↗</a>`:""}</td>
        <td>${st}</td>
        <td class="srcline">${esc(a.fx)}</td>
      </tr>`;
    }).join("");
  }

  /* ---------- QUESTIONS ---------- */
  function renderQuestions(){
    const el = document.getElementById("question-list");
    el.innerHTML = QUESTIONS.map((q,i)=>`
      <article class="card" style="margin:10px 0">
        <h3>${i+1}. ${esc(q.q)} ${q.st==="open"?`<span class="chip f">open</span>`:`<span class="chip v">answered</span>`}</h3>
        <p class="sub" style="margin:6px 0 4px"><strong>Why it blocks a decision:</strong> ${esc(q.why)}</p>
        <p class="sub" style="margin:4px 0"><strong>What we know today:</strong> ${esc(q.now)}</p>
        <p class="sub" style="margin:4px 0"><strong>Action to close it:</strong> ${esc(q.action)}</p>
      </article>`).join("");
  }

  /* ---------- FILTERS ---------- */
  function wireFilters(){
    document.querySelectorAll("[data-filter-input]").forEach(inp=>{
      const table = document.querySelector(inp.dataset.filterInput);
      if(!table) return;
      const apply = ()=>{
        const q = inp.value.trim().toLowerCase();
        table.querySelectorAll("tbody tr").forEach(tr=>{
          tr.hidden = q ? !(tr.dataset.f||"").includes(q) : false;
        });
      };
      inp.addEventListener("input", apply);
    });
  }

  document.addEventListener("DOMContentLoaded", mount);
})();
