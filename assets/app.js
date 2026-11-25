(function () {
  const NAV_ITEMS = [
    { href: './index.html', label: 'Summary', id: 'summary' },
    { href: './hotels.html', label: 'Hotels (15)', id: 'hotels' },
    { href: './restaurants.html', label: 'MICHELIN (37)', id: 'restaurants' },
    { href: './activities.html', label: 'Activities (24)', id: 'activities' },
    { href: './questions.html', label: 'Trip Estimator & Qs', id: 'questions' },
    { href: './suggestions.html', label: 'Suggestions', id: 'suggestions' },
    { href: './flagged.html', label: 'Audit & Flags', id: 'flagged' }
  ];

  window.renderChrome = function (activeId) {
    const header = document.getElementById('site-header');
    if (header) {
      header.innerHTML = `
        <div class="container header-inner">
          <a class="brand" href="./index.html" style="text-decoration:none">
            <span class="brand-mark">CF1</span>
            <span>ChinaFun1 <span class="brand-sub">Feb–Mar 2027 · 2 Adults</span></span>
          </a>
          <nav class="nav-pills" aria-label="Primary navigation">
            ${NAV_ITEMS.map(item => `
              <a href="${item.href}" class="${item.id === activeId ? 'active' : ''}">${item.label}</a>
            `).join('')}
          </nav>
        </div>
      `;
    }
    const footer = document.getElementById('site-footer');
    if (footer) {
      footer.innerHTML = `
        <div class="container footer-inner">
          <div>Verified Nov 25, 2026 · FX anchored: <strong>1 USD = 6.6775 CNY = 7.84 HKD</strong> · All hotel quotes verified for 2 adults, 7 nights (private bath, &ge; Queen bed).</div>
          <div><a href="./flagged.html">Verification Audit &amp; Exclusions</a> · <a href="./data/hotels.json">JSON Data</a></div>
        </div>
      `;
    }
  };

  window.loadData = async function () {
    const [hotelsRes, restRes, actRes, flagRes] = await Promise.all([
      fetch('./data/hotels.json'),
      fetch('./data/restaurants.json'),
      fetch('./data/activities.json'),
      fetch('./data/flagged.json')
    ]);
    if (!hotelsRes.ok || !restRes.ok || !actRes.ok || !flagRes.ok) {
      throw new Error('Failed loading verified JSON datasets.');
    }
    return {
      hotelsData: await hotelsRes.json(),
      restData: await restRes.json(),
      actData: await actRes.json(),
      flagData: await flagRes.json()
    };
  };

  window.fmtUSD = function (n) {
    if (n === null || n === undefined) return '—';
    return '$' + Number(n).toLocaleString('en-US');
  };

  window.tierBadge = function (tier) {
    if (tier.includes('3 Star')) return `<span class="badge badge-star">★★★ ${tier}</span>`;
    if (tier.includes('2 Star')) return `<span class="badge badge-star">★★ ${tier}</span>`;
    if (tier.includes('1 Star')) return `<span class="badge badge-star">★ ${tier}</span>`;
    if (tier.includes('Bib')) return `<span class="badge badge-bib">Bib Gourmand</span>`;
    return `<span class="badge badge-selected">${tier}</span>`;
  };

  window.transitBadge = function (mins) {
    if (mins === null || mins === undefined) return '';
    if (mins <= 15) return `<span class="badge badge-green">${mins} min (Walk / 1–2 stops)</span>`;
    if (mins <= 30) return `<span class="badge badge-amber">${mins} min (Direct / 1-xfer)</span>`;
    return `<span class="badge badge-blue">${mins} min (&le;60 min)</span>`;
  };

  window.socialChips = function (item, primaryLabel) {
    const out = [];
    if (item.michelin_url) out.push(`<a class="chip-link" target="_blank" rel="noopener" href="${item.michelin_url}">MICHELIN</a>`);
    if (item.official_url) out.push(`<a class="chip-link" target="_blank" rel="noopener" href="${item.official_url}">${primaryLabel || 'Official'}</a>`);
    if (item.booking_url) out.push(`<a class="chip-link" target="_blank" rel="noopener" href="${item.booking_url}">Booking.com</a>`);
    if (item.youtube_url) out.push(`<a class="chip-link yt" target="_blank" rel="noopener" href="${item.youtube_url}">YouTube</a>`);
    if (item.instagram_url) out.push(`<a class="chip-link ig" target="_blank" rel="noopener" href="${item.instagram_url}">Instagram</a>`);
    if (item.tiktok_url) out.push(`<a class="chip-link tt" target="_blank" rel="noopener" href="${item.tiktok_url}">TikTok</a>`);
    return out.join('');
  };

  window.esc = function (s) {
    return String(s ?? '').replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[c]);
  };
})();
