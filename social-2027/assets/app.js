(function () {
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  document.querySelectorAll('[data-filter-table]').forEach(function (input) {
    var table = document.querySelector('table.' + input.getAttribute('data-filter-table'));
    if (!table) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      table.querySelectorAll('tbody tr').forEach(function (row) {
        row.hidden = q !== '' && row.textContent.toLowerCase().indexOf(q) === -1;
      });
    });
  });
})();
