(()=>{
  const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
  const html=document.documentElement;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine=matchMedia('(pointer:fine)').matches;
  const clamp=(v,a=0,b=1)=>Math.min(b,Math.max(a,v));
  const ease=t=>1-Math.pow(1-t,3);
  const store=(k,v)=>{try{v===undefined?sessionStorage.removeItem(k):sessionStorage.setItem(k,v)}catch(e){}};

  /* ---------- Split-text headline reveals ---------- */
  const splitEls=$$('.cinematic-copy h1,.section-head h2,.page-hero h1,.intro-sticky h2,.portfolio-copy h2,.cta-band h2,.story-grid h2,.not-found h1,.showreel-caption h2,.contact-cards h2,.faq-section h2,.data-care h2');
  const split=el=>{
    let i=0;
    const unit=()=>{const w=document.createElement('span');w.className='w';const inner=document.createElement('span');inner.className='wi';inner.style.setProperty('--i',i++);w.appendChild(inner);return [w,inner]};
    const walk=node=>[...node.childNodes].forEach(n=>{
      if(n.nodeType===3){
        const frag=document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(p=>{if(!p)return;if(/^\s+$/.test(p)){frag.appendChild(document.createTextNode(' '));return}const [w,inner]=unit();inner.textContent=p;frag.appendChild(w)});
        n.replaceWith(frag);
      }else if(n.nodeType===1&&n.tagName!=='BR'){
        const cs=getComputedStyle(n);
        if((cs.webkitBackgroundClip||cs.backgroundClip)==='text'){const [w,inner]=unit();n.replaceWith(w);inner.appendChild(n)}else walk(n);
      }
    });
    walk(el);el.classList.add('split');
  };
  if(!reduce){
    splitEls.forEach(split);
    const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target;const go=()=>el.classList.add('split-in');if(el.closest('[data-cinematic-hero]')&&!html.classList.contains('is-ready'))document.addEventListener('bc:ready',go,{once:true});else go();io.unobserve(el)}),{threshold:.2});
    splitEls.forEach(el=>io.observe(el));
  }

  /* ---------- Intro splash ---------- */
  const splash=$('[data-splash]');
  const heroVideo=$('.hero-video');
  const ready=()=>{if(html.classList.contains('is-ready'))return;html.classList.add('is-ready');html.classList.remove('splash-on');document.dispatchEvent(new Event('bc:ready'))};
  if(splash&&html.classList.contains('splash-on')){
    store('bc-intro','1');
    const count=$('[data-splash-count]'),bar=$('[data-splash-bar]'),sv=$('video',splash);
    sv?.play?.().catch(()=>{});
    const D=2700,t0=performance.now();let done=false;
    const finish=()=>{splash.classList.add('out');try{if(heroVideo&&sv&&sv.currentTime)heroVideo.currentTime=sv.currentTime}catch(e){}ready();setTimeout(()=>splash.remove(),1100)};
    const expand=()=>{if(done)return;done=true;splash.classList.add('expand');setTimeout(finish,950)};
    const tick=now=>{if(done)return;const p=clamp((now-t0)/D),e=ease(p);count.textContent=String(Math.round(e*100)).padStart(3,'0');bar.style.transform=`scaleX(${e})`;if(p<1)requestAnimationFrame(tick);else expand()};
    requestAnimationFrame(tick);
    $('[data-splash-skip]')?.addEventListener('click',()=>{done=true;finish()});
  }else{splash?.remove();requestAnimationFrame(ready)}

  /* ---------- Page transition curtain ---------- */
  const curtain=$('[data-curtain]');
  if(curtain){
    if(html.classList.contains('from-nav'))requestAnimationFrame(()=>{curtain.classList.add('leave');html.classList.remove('from-nav')});
    document.addEventListener('click',e=>{
      const a=e.target.closest('a[href]');
      if(!a||reduce||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button!==0)return;
      const url=new URL(a.href,location.href);
      if(a.target==='_blank'||a.hasAttribute('download')||url.origin!==location.origin||url.pathname.startsWith('/admin'))return;
      if(url.pathname===location.pathname&&(url.hash||url.href===location.href))return;
      e.preventDefault();store('bc-nav','1');
      curtain.classList.remove('leave');curtain.classList.add('enter');
      setTimeout(()=>{location.href=url.href},560);
    });
    addEventListener('pageshow',e=>{if(e.persisted){curtain.classList.remove('enter');curtain.classList.add('leave')}});
  }

  /* ---------- Scroll-driven effects ---------- */
  const bar=$('[data-scroll-progress]');
  const reel=$('[data-showreel]'),frame=$('[data-showreel-frame]');
  const mega=$('[data-footer-mega]');
  let ticking=false;
  const onScroll=()=>{
    ticking=false;
    const max=document.documentElement.scrollHeight-innerHeight;
    if(bar)bar.style.transform=`scaleX(${clamp(scrollY/Math.max(1,max))})`;
    if(reel&&frame&&!reduce){const r=reel.getBoundingClientRect();const p=clamp(-r.top/Math.max(1,r.height-innerHeight));frame.style.setProperty('--e',ease(clamp(p/.55)).toFixed(4));frame.style.setProperty('--p',p.toFixed(4))}
    if(mega&&!reduce){const r=mega.getBoundingClientRect();mega.style.setProperty('--m',clamp(1-(r.top-innerHeight*.35)/(innerHeight*.65)).toFixed(3))}
  };
  const req=()=>{if(!ticking){ticking=true;requestAnimationFrame(onScroll)}};
  addEventListener('scroll',req,{passive:true});addEventListener('resize',req);req();

  /* ---------- Video: timecode + chapters + lazy play ---------- */
  const tc=$('[data-timecode]');
  const fmt=t=>{const s=Math.floor(t),f=Math.floor((t-s)*24);return `00:${String(s).padStart(2,'0')}:${String(f).padStart(2,'0')}`};
  if(heroVideo&&tc)heroVideo.addEventListener('timeupdate',()=>{tc.textContent=fmt(heroVideo.currentTime)});
  const reelVideo=$('video',reel||document.createElement('div'));
  const chapters=$$('[data-chapter]');
  if(reelVideo){
    reelVideo.addEventListener('timeupdate',()=>{const idx=Math.min(3,Math.floor(reelVideo.currentTime/4.1));chapters.forEach((c,i)=>c.classList.toggle('active',i===idx));const cp=$('[data-reel-progress]');if(cp&&reelVideo.duration)cp.style.transform=`scaleX(${reelVideo.currentTime/reelVideo.duration})`});
    chapters.forEach((c,i)=>c.addEventListener('click',()=>{reelVideo.currentTime=i*4.1+.05;reelVideo.play().catch(()=>{})}));
    const vio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){if(!reelVideo.src&&reelVideo.dataset.src){reelVideo.src=reelVideo.dataset.src}reelVideo.play().catch(()=>{})}else reelVideo.pause()}),{threshold:.15});
    vio.observe(reelVideo);
  }

  /* ---------- Staggered children ---------- */
  $$('.service-grid,.value-grid,.model-grid,.process-track,.team-grid,.contact-pair,.stat-strip,.service-detail-list,.faq-list').forEach(g=>[...g.children].forEach((c,i)=>c.style.setProperty('--stagger',i)));

  /* ---------- Section fly-in for non-reveal blocks ---------- */
  const flyEls=$$('.service-card,.model-grid article,.team-grid .person-card,.contact-pair article,.service-detail,.faq-list details,.data-care,.form-card,.prose>*');
  if(!reduce){const fio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('fly-in');fio.unobserve(e.target)}}),{threshold:.1,rootMargin:'0px 0px -5%'});flyEls.forEach(el=>{el.classList.add('fly');fio.observe(el)})}

  if(reduce||!fine)return;

  /* ---------- Pointer effects (desktop only) ---------- */
  const spotSel='.service-card,.scene-card,.value-grid article,.process-step,.model-grid article,.person-card,.contact-pair article,.service-detail,.form-card,.review-card,.review-empty,.portfolio-card,.stat-strip>div';
  $$(spotSel).forEach(el=>{
    if(getComputedStyle(el).position==='static')el.style.position='relative';
    const g=document.createElement('span');g.className='spot-glow';g.setAttribute('aria-hidden','true');el.appendChild(g);el.classList.add('spot');
    el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect();el.style.setProperty('--sx',`${e.clientX-r.left}px`);el.style.setProperty('--sy',`${e.clientY-r.top}px`)});
  });

  $$('.btn.primary,.btn.light,.floating-whatsapp,.icon-btn').forEach(b=>{
    b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();const x=(e.clientX-r.left-r.width/2)*.22,y=(e.clientY-r.top-r.height/2)*.3;b.style.translate=`${x.toFixed(1)}px ${y.toFixed(1)}px`});
    b.addEventListener('pointerleave',()=>{b.style.translate=''});
  });

  const heroEl=$('[data-cinematic-hero]');
  if(heroEl&&heroVideo)heroEl.addEventListener('pointermove',e=>{const x=(e.clientX/innerWidth-.5),y=(e.clientY/innerHeight-.5);heroVideo.style.setProperty('--hx',`${(-x*22).toFixed(1)}px`);heroVideo.style.setProperty('--hy',`${(-y*16).toFixed(1)}px`)});

  const ring=document.createElement('div');ring.className='cursor-ring';ring.setAttribute('aria-hidden','true');ring.innerHTML='<span></span>';
  const dot=document.createElement('div');dot.className='cursor-dot';dot.setAttribute('aria-hidden','true');
  document.body.append(ring,dot);
  let mx=innerWidth/2,my=innerHeight/2,rx=mx,ry=my,shown=false;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;dot.style.transform=`translate(${mx}px,${my}px)`;if(!shown){shown=true;html.classList.add('cursor-on')}
    const t=e.target.closest?.('a,button,summary,label,[data-tilt],input,select,textarea');
    const view=e.target.closest?.('.service-card,.portfolio-card,.scene-card');
    ring.classList.toggle('hover',!!t);ring.classList.toggle('view',!!view);
    ring.querySelector('span').textContent=view?'Explore':'';
  },{passive:true});
  document.addEventListener('pointerleave',()=>html.classList.remove('cursor-on'));
  document.addEventListener('pointerenter',()=>html.classList.add('cursor-on'));
  const loop=()=>{rx+=(mx-rx)*.18;ry+=(my-ry)*.18;ring.style.transform=`translate(${rx}px,${ry}px)`;requestAnimationFrame(loop)};loop();
})();
