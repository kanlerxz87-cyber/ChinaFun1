// Minimal JS: close mobile menu on outside click
document.addEventListener('click', (e) => {
  if (!document.body.classList.contains('menu-open')) return;
  const top = document.querySelector('.topbar');
  if (top && !top.contains(e.target)) document.body.classList.remove('menu-open');
});
