(()=>{
  const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
  const esc=(v='')=>String(v).replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));

  const header=$('[data-header]');
  const onScroll=()=>header?.classList.toggle('scrolled',scrollY>8); onScroll(); addEventListener('scroll',onScroll,{passive:true});

  const menuBtn=$('[data-menu-toggle]'), mobileMenu=$('[data-mobile-menu]');
  menuBtn?.addEventListener('click',()=>{const open=menuBtn.getAttribute('aria-expanded')!=='true';menuBtn.setAttribute('aria-expanded',String(open));mobileMenu?.classList.toggle('open',open)});
  $$('[data-mobile-menu] a').forEach(a=>a.addEventListener('click',()=>{menuBtn?.setAttribute('aria-expanded','false');mobileMenu?.classList.remove('open')}));

  const themeBtn=$('[data-theme-toggle]');
  themeBtn?.addEventListener('click',()=>{const next=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=next;try{localStorage.setItem('buddy-theme',next)}catch(e){}});

  if(!matchMedia('(prefers-reduced-motion: reduce)').matches){
    const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
    $$('.reveal').forEach(el=>io.observe(el));
  } else $$('.reveal').forEach(el=>el.classList.add('in'));

  const contactModal=$('[data-contact-modal]'), enquiryModal=$('[data-enquiry-modal]');
  let modalMessage='Hi, I need help from Buddy Computers.';
  function setWaLinks(msg){
    const text=encodeURIComponent(msg||modalMessage);
    $('[data-wa-navin]')?.setAttribute('href',`https://wa.me/917096310195?text=${text}`);
    $('[data-wa-shubham]')?.setAttribute('href',`https://wa.me/917426933642?text=${text}`);
  }
  function openDialog(d){if(!d)return; if(typeof d.showModal==='function')d.showModal(); else d.setAttribute('open','')}
  $$('[data-whatsapp-open]').forEach(b=>b.addEventListener('click',()=>{modalMessage='Hi, I need help from Buddy Computers.';setWaLinks(modalMessage);openDialog(contactModal)}));
  $('[data-modal-close]')?.addEventListener('click',()=>contactModal?.close());
  contactModal?.addEventListener('click',e=>{if(e.target===contactModal)contactModal.close()});

  $$('[data-enquiry-open]').forEach(b=>b.addEventListener('click',()=>{
    openDialog(enquiryModal);
    const service=b.dataset.service; if(service){const sel=$('select[name="service"]',enquiryModal); if(sel) sel.value=service}
  }));
  $('[data-enquiry-close]')?.addEventListener('click',()=>enquiryModal?.close());
  enquiryModal?.addEventListener('click',e=>{if(e.target===enquiryModal)enquiryModal.close()});

  async function firebase(){ return import('/assets/firebase-public.js') }
  function formData(form){const fd=new FormData(form);return Object.fromEntries(fd.entries())}
  function setStatus(form,msg,type=''){const el=$('.form-status',form);if(!el)return;el.textContent=msg;el.className=`form-status ${type}`.trim()}
  function cleanPhone(v){return String(v||'').replace(/[^0-9+]/g,'').slice(0,20)}
  function fallbackWhatsApp(data){
    modalMessage=`Hi, I need help from Buddy Computers.\n\nName: ${data.name||''}\nPhone: ${data.phone||''}\nService: ${data.service||'Not sure'}\nDetails: ${data.message||''}`;
    setWaLinks(modalMessage);openDialog(contactModal)
  }

  $$('[data-enquiry-form]').forEach(form=>form.addEventListener('submit',async e=>{
    e.preventDefault(); if(form.website?.value) return;
    const btn=$('button[type="submit"]',form), d=formData(form); d.phone=cleanPhone(d.phone); d.context=form.dataset.context||'website'; d.page=location.pathname; d.preference=d.preference||'WhatsApp'; d.email=d.email||'';
    if(d.phone.replace(/\D/g,'').length<10){setStatus(form,'Please enter a valid mobile number.','error');return}
    btn.disabled=true;setStatus(form,'Sending your enquiry…');
    try{
      const fb=await firebase();
      if(!fb.firebaseConfigured){setStatus(form,'Firebase setup is pending. Choose a WhatsApp contact to send this enquiry.','error');fallbackWhatsApp(d);return}
      await fb.submitEnquiry({name:String(d.name).trim(),phone:d.phone,email:String(d.email).trim(),service:d.service,preference:d.preference,message:String(d.message).trim(),context:d.context,page:d.page});
      form.reset();setStatus(form,'Thanks — your enquiry has been received. We’ll contact you soon.','success');
      setTimeout(()=>{if(form.closest('dialog')?.open)form.closest('dialog').close()},1600);
    }catch(err){console.error(err);setStatus(form,'We could not save the enquiry right now. Please use WhatsApp or call us.','error');fallbackWhatsApp(d)}finally{btn.disabled=false}
  }));

  $$('[data-review-form]').forEach(form=>form.addEventListener('submit',async e=>{
    e.preventDefault(); if(form.website?.value) return;
    const btn=$('button[type="submit"]',form),d=formData(form);btn.disabled=true;setStatus(form,'Submitting your review…');
    try{
      const fb=await firebase();
      if(!fb.firebaseConfigured){setStatus(form,'Review submission will be available after Firebase is connected.','error');return}
      await fb.submitReview({name:String(d.name).trim(),service:d.service,rating:Number(d.rating),message:String(d.message).trim(),page:location.pathname});
      form.reset();setStatus(form,'Thank you. Your review is pending approval and will appear after moderation.','success');
    }catch(err){console.error(err);setStatus(form,'We could not submit the review right now. Please try again later.','error')}finally{btn.disabled=false}
  }));

  function fmtDate(v){try{const dt=v?.toDate?v.toDate():v?.seconds?new Date(v.seconds*1000):null;return dt?new Intl.DateTimeFormat('en-IN',{day:'numeric',month:'short',year:'numeric'}).format(dt):''}catch{return ''}}
  function reviewHTML(r){
    const initial=esc((r.name||'?').trim().charAt(0).toUpperCase());const rating=Math.max(1,Math.min(5,Number(r.rating)||5));
    return `<article class="review-card"><div class="review-top"><div class="review-person"><div class="review-avatar">${initial}</div><div><strong>${esc(r.name)}</strong><small>${esc(r.service||'Customer')}</small></div></div><div class="stars" aria-label="${rating} out of 5 stars">${'★'.repeat(rating)}${'☆'.repeat(5-rating)}</div></div><blockquote>“${esc(r.message)}”</blockquote><time>${esc(fmtDate(r.createdAt))}</time></article>`
  }
  $$('[data-approved-reviews]').forEach(async box=>{
    const limit=Number(box.dataset.limit)||999; box.classList.add('loading');
    try{const fb=await firebase();if(!fb.firebaseConfigured)return;const rs=(await fb.getApprovedReviews()).slice(0,limit);if(rs.length)box.innerHTML=rs.map(reviewHTML).join('')}
    catch(err){console.warn('Reviews unavailable',err)}finally{box.classList.remove('loading')}
  });
})();
