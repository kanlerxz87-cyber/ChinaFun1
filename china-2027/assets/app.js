(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("siteNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Generic filterable list/table engine (used on restaurants.html & activities.html)
  var filterRoot = document.querySelector("[data-filter-root]");
  if (filterRoot) {
    var searchEl = filterRoot.querySelector("[data-filter-search]");
    var selects = Array.prototype.slice.call(filterRoot.querySelectorAll("select[data-filter-key]"));
    var resetBtn = filterRoot.querySelector("[data-filter-reset]");
    var countEl = filterRoot.querySelector("[data-filter-count]");
    var rows = Array.prototype.slice.call(document.querySelectorAll("[data-filter-item]"));

    function applyFilters() {
      var q = searchEl ? searchEl.value.trim().toLowerCase() : "";
      var visible = 0;
      rows.forEach(function (row) {
        var match = true;
        if (q) {
          var hay = (row.getAttribute("data-search") || "").toLowerCase();
          if (hay.indexOf(q) === -1) match = false;
        }
        if (match) {
          for (var i = 0; i < selects.length; i++) {
            var key = selects[i].getAttribute("data-filter-key");
            var val = selects[i].value;
            if (!val) continue;
            var rv = row.getAttribute("data-" + key) || "";
            if (val === "__nonempty__") {
              if (!rv || rv === "0" || rv === "no") { match = false; break; }
            } else if (rv !== val) {
              match = false;
              break;
            }
          }
        }
        row.style.display = match ? "" : "none";
        if (match) visible++;
      });
      if (countEl) {
        countEl.textContent = "Showing " + visible + " of " + rows.length;
      }
    }

    if (searchEl) searchEl.addEventListener("input", applyFilters);
    selects.forEach(function (s) { s.addEventListener("change", applyFilters); });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        if (searchEl) searchEl.value = "";
        selects.forEach(function (s) { s.value = ""; });
        applyFilters();
      });
    }
    applyFilters();
  }

  // Tabs (used on itineraries.html)
  var tabBtns = Array.prototype.slice.call(document.querySelectorAll("[data-tab-target]"));
  if (tabBtns.length) {
    var panels = Array.prototype.slice.call(document.querySelectorAll("[data-tab-panel]"));
    tabBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-tab-target");
        tabBtns.forEach(function (b) { b.classList.toggle("active", b === btn); });
        panels.forEach(function (p) {
          p.classList.toggle("active", p.getAttribute("data-tab-panel") === target);
        });
      });
    });
  }
})();
