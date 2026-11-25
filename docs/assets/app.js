// Small progressive-enhancement layer: mobile nav + per-table search filter.
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Add a filter box above every large table.
  document.querySelectorAll('table').forEach(function (tbl) {
    if (tbl.rows.length < 6) return;
    var wrap = tbl.closest('.tablewrap');
    if (!wrap || wrap.dataset.filtered) return;
    wrap.dataset.filtered = '1';
    var bar = document.createElement('div');
    bar.className = 'filterbar';
    bar.innerHTML = '<input type="search" placeholder="Filter rows… (restaurant, district, cuisine)" aria-label="Filter table rows">' +
                    '<span class="count"></span>';
    wrap.parentNode.insertBefore(bar, wrap);
    var input = bar.querySelector('input');
    var count = bar.querySelector('.count');
    var rows = Array.prototype.slice.call(tbl.tBodies[0].rows);
    function update() {
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (r) {
        var hit = !q || r.textContent.toLowerCase().indexOf(q) !== -1;
        r.style.display = hit ? '' : 'none';
        if (hit) shown++;
      });
      count.textContent = shown + ' / ' + rows.length + ' rows';
    }
    input.addEventListener('input', update);
    update();
  });

  // Make table headers sticky-friendly on horizontal scroll: highlight row under cursor.
  document.querySelectorAll('tbody tr').forEach(function (tr) {
    tr.addEventListener('mouseenter', function () {
      Array.prototype.forEach.call(tr.cells, function (c) { c.style.background = '#fcfcfd'; });
    });
    tr.addEventListener('mouseleave', function () {
      Array.prototype.forEach.call(c.cells || tr.cells, function (c) { c.style.background = ''; });
    });
  });
})();
