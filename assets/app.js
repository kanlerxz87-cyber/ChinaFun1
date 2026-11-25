/* ChinaFun1 dashboard behaviour. Progressive enhancement: every table and page
   is fully readable with JavaScript disabled. No external libraries. */
(function () {
  "use strict";

  /* ---- mobile navigation ---- */
  var btn = document.querySelector(".navtoggle");
  var list = document.getElementById("nav-list");
  if (btn && list) {
    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", function () {
      var open = list.classList.toggle("hidden") === false;
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close menu" : "Menu";
    });
  }

  /* ---- row counter + text filter + select filters per table ---- */
  function wireTable(wrap) {
    var table = wrap.querySelector("table[data-filterable]");
    if (!table) return;
    var body = table.tBodies[0];
    if (!body) return;
    var rows = Array.prototype.slice.call(body.rows);
    var input = wrap.querySelector("input[data-search]");
    var selects = wrap.querySelectorAll("select[data-col]");
    var out = wrap.querySelector(".count");

    function apply() {
      var q = (input && input.value ? input.value : "").trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (tr) {
        var okText = !q || tr.textContent.toLowerCase().indexOf(q) !== -1;
        var okSel = true;
        selects.forEach(function (sel) {
          if (!sel.value) return;
          var idx = parseInt(sel.getAttribute("data-col"), 10);
          var cell = tr.cells[idx];
          if (!cell) { okSel = false; return; }
          okSel = okSel && cell.textContent.trim().toLowerCase() === sel.value.toLowerCase();
        });
        var show = okText && okSel;
        tr.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (out) out.textContent = shown + " of " + rows.length + " rows shown";
    }

    if (input) input.addEventListener("input", apply);
    selects.forEach(function (s) { s.addEventListener("change", apply); });
    apply();
  }

  /* ---- click-to-sort on <th data-sort> ---- */
  function wireSort(table) {
    var heads = table.querySelectorAll("th[data-sort]");
    heads.forEach(function (th, colIdx) {
      th.style.cursor = "pointer";
      th.title = "Sort by this column";
      var idx = th.getAttribute("data-sort-col");
      var col = idx === null ? Array.prototype.indexOf.call(th.parentNode.children, th) : parseInt(idx, 10);
      th.addEventListener("click", function () {
        var body = table.tBodies[0];
        if (!body) return;
        var rows = Array.prototype.slice.call(body.rows);
        var asc = th.getAttribute("data-dir") !== "asc";
        heads.forEach(function (h) { h.removeAttribute("data-dir"); });
        th.setAttribute("data-dir", asc ? "asc" : "desc");
        rows.sort(function (a, b) {
          var ca = a.cells[col], cb = b.cells[col];
          var va = ca ? ca.getAttribute("data-v") || ca.textContent.trim() : "";
          var vb = cb ? cb.getAttribute("data-v") || cb.textContent.trim() : "";
          var na = parseFloat(String(va).replace(/[^0-9.\-]/g, ""));
          var nb = parseFloat(String(vb).replace(/[^0-9.\-]/g, ""));
          var both = !isNaN(na) && !isNaN(nb);
          if (both) return asc ? na - nb : nb - na;
          return asc ? String(va).localeCompare(String(vb)) : String(vb).localeCompare(String(va));
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
  }

  document.querySelectorAll("[data-tablewrap]").forEach(wireTable);
  document.querySelectorAll("table[data-sortable] th[data-sort]").length &&
    document.querySelectorAll("table[data-sortable]").forEach(wireSort);

  /* ---- "back to top" on long table pages ---- */
  document.querySelectorAll("[data-top]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
})();
