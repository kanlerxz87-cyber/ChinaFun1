const nav=document.getElementById('nav'), btn=document.getElementById('navtoggle');
if(btn&&nav){btn.addEventListener('click',()=>{const open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false')});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');btn.setAttribute('aria-expanded','false')}))}
document.querySelectorAll('.filter').forEach(input=>{input.addEventListener('input',()=>{
  const q=input.value.toLowerCase().trim(); const wrap=input.parentElement.nextElementSibling;
  if(!wrap||!wrap.classList.contains('tablewrap'))return;
  wrap.querySelectorAll('tbody tr').forEach(tr=>{tr.style.display=tr.textContent.toLowerCase().includes(q)?'':'none'})})});
