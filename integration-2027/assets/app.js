/* Tiny progressive enhancement: client-side table/card filtering. No dependencies. */
(function(){
  function apply(){
    var input = this;
    var target = document.querySelector(input.dataset.filterInput);
    if(!target) return;
    var q = input.value.trim().toLowerCase();
    var items = target.tagName === 'TABLE' && target.tBodies[0]
      ? Array.prototype.slice.call(target.tBodies[0].rows)
      : Array.prototype.slice.call(target.children);
    items.forEach(function(el){ el.hidden = !!q && (el.dataset.f || '').indexOf(q) === -1; });
  }
  document.querySelectorAll('[data-filter-input]').forEach(function(inp){
    inp.addEventListener('input', apply);
  });
})();
