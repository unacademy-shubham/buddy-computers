import '/assets/firebase-config.js';

const cfg=window.BUDDY_FIREBASE_CONFIG||{};
const configured=Boolean(cfg.apiKey&&cfg.projectId&&!String(cfg.apiKey).startsWith('YOUR_')&&!String(cfg.projectId).startsWith('YOUR_'));
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=(v='')=>String(v).replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const login=$('[data-admin-login]'),dashboard=$('[data-admin-dashboard]'),setup=$('[data-admin-setup-note]'),loginForm=$('[data-admin-login-form]'),loginStatus=$('[data-admin-login-status]');
if(!configured) setup.hidden=false;
let auth,db,fs,authMod,unsub, enquiries=[],reviews=[];

function status(el,msg,type=''){el.textContent=msg;el.className=`form-status ${type}`.trim()}
function toast(msg,type=''){const el=$('[data-toast]');el.textContent=msg;el.className=`toast show ${type}`.trim();clearTimeout(el._t);el._t=setTimeout(()=>el.className='toast',2400)}
function fmt(v){try{const d=v?.toDate?v.toDate():v?.seconds?new Date(v.seconds*1000):null;return d?new Intl.DateTimeFormat('en-IN',{day:'2-digit',month:'short',year:'numeric',hour:'numeric',minute:'2-digit'}).format(d):'—'}catch{return '—'}}
function ms(v){return v?.toMillis?v.toMillis():v?.seconds?v.seconds*1000:0}
function isAdmin(user){return !!user&&String(user.email||'').toLowerCase()===String(window.BUDDY_ADMIN_EMAIL||'').toLowerCase()}

async function loadSdk(){
  if(!configured) return false;
  const [appMod,aMod,fMod]=await Promise.all([
    import('https://www.gstatic.com/firebasejs/11.10.0/firebase-app.js'),
    import('https://www.gstatic.com/firebasejs/11.10.0/firebase-auth.js'),
    import('https://www.gstatic.com/firebasejs/11.10.0/firebase-firestore.js')
  ]);
  const app=appMod.getApps().length?appMod.getApp():appMod.initializeApp(cfg); auth=aMod.getAuth(app);db=fMod.getFirestore(app);fs=fMod;authMod=aMod;return true;
}

function showLogin(){login.hidden=false;dashboard.hidden=true;if(unsub){unsub.forEach?.(u=>u());unsub=null}}
function showDashboard(user){login.hidden=true;dashboard.hidden=false;$('[data-admin-email]').textContent=user.email||'Admin';subscribeData()}

if(configured){
  loadSdk().then(()=>authMod.onAuthStateChanged(auth,user=>{
    if(user&&isAdmin(user))showDashboard(user);else{if(user)authMod.signOut(auth);showLogin()}
  })).catch(e=>{console.error(e);status(loginStatus,'Could not connect to Firebase. Check the config.','error')});
}
loginForm?.addEventListener('submit',async e=>{
  e.preventDefault();if(!configured){status(loginStatus,'Firebase is not configured yet. Follow FIREBASE_SETUP.md.','error');return}
  const fd=new FormData(loginForm);status(loginStatus,'Signing in…');
  try{const c=await authMod.signInWithEmailAndPassword(auth,fd.get('email'),fd.get('password'));if(!isAdmin(c.user)){await authMod.signOut(auth);throw new Error('This account is not authorised for the Buddy Computers admin panel.')}status(loginStatus,'','')}
  catch(err){console.error(err);status(loginStatus,err.message?.includes('auth/')?'Email or password is incorrect.':err.message||'Sign in failed.','error')}
});
$('[data-reset-password]')?.addEventListener('click',async()=>{
  if(!configured){status(loginStatus,'Configure Firebase first.','error');return}const email=loginForm.email.value||window.BUDDY_ADMIN_EMAIL;
  try{await authMod.sendPasswordResetEmail(auth,email);status(loginStatus,'Password reset email sent.','success')}catch(e){status(loginStatus,'Could not send a reset email. Check the account email.','error')}
});
$('[data-admin-logout]')?.addEventListener('click',()=>authMod?.signOut(auth));

function subscribeData(){
  if(unsub)unsub.forEach?.(u=>u());
  const a=fs.onSnapshot(fs.collection(db,'enquiries'),snap=>{enquiries=snap.docs.map(d=>({id:d.id,...d.data()})).sort((x,y)=>ms(y.createdAt)-ms(x.createdAt));renderAll()},e=>{console.error(e);toast('Could not load enquiries','error')});
  const b=fs.onSnapshot(fs.collection(db,'reviews'),snap=>{reviews=snap.docs.map(d=>({id:d.id,...d.data()})).sort((x,y)=>ms(y.createdAt)-ms(x.createdAt));renderAll()},e=>{console.error(e);toast('Could not load reviews','error')});
  unsub=[a,b];
}
function renderAll(){
  const newE=enquiries.filter(x=>x.status==='new').length,pendingR=reviews.filter(x=>x.status==='pending').length,approved=reviews.filter(x=>x.status==='approved').length;
  $('[data-stat-new-enquiries]').textContent=newE;$('[data-stat-pending-reviews]').textContent=pendingR;$('[data-stat-approved-reviews]').textContent=approved;$('[data-stat-total-enquiries]').textContent=enquiries.length;
  $('[data-enquiry-badge]').textContent=newE;$('[data-review-badge]').textContent=pendingR;renderEnquiries();renderReviews();renderActivity();
}
function filterList(list,q,status,fields){q=q.trim().toLowerCase();return list.filter(x=>(status==='all'||x.status===status)&&(!q||fields.some(f=>String(x[f]||'').toLowerCase().includes(q))))}
function enquiryActions(e){return `<div class="row-actions">${e.status!=='contacted'?`<button data-e-status="contacted" data-id="${e.id}">Contacted</button>`:''}${e.status!=='resolved'?`<button data-e-status="resolved" data-id="${e.id}">Resolve</button>`:''}${e.status!=='new'?`<button data-e-status="new" data-id="${e.id}">Reopen</button>`:''}<button class="danger" data-e-delete data-id="${e.id}">Delete</button></div>`}
function reviewActions(r){return `<div class="row-actions">${r.status!=='approved'?`<button data-r-status="approved" data-id="${r.id}">Approve</button>`:''}${r.status!=='rejected'?`<button data-r-status="rejected" data-id="${r.id}">Reject</button>`:''}${r.status!=='pending'?`<button data-r-status="pending" data-id="${r.id}">Pending</button>`:''}<button class="danger" data-r-delete data-id="${r.id}">Delete</button></div>`}
function renderEnquiries(){const q=$('[data-enquiry-search]')?.value||'',st=$('[data-enquiry-filter]')?.value||'all',items=filterList(enquiries,q,st,['name','phone','email','service','message','preference']);const tb=$('[data-enquiry-table]'),cards=$('[data-enquiry-cards]');if(!tb||!cards)return;if(!items.length){tb.innerHTML='<tr><td colspan="5" class="empty-state">No enquiries found.</td></tr>';cards.innerHTML='<div class="empty-state">No enquiries found.</div>';return}tb.innerHTML=items.map(e=>`<tr><td><div class="record-customer"><strong>${esc(e.name)}</strong><span>${esc(e.phone)}</span><span>${esc(e.email||'')}</span></div></td><td><div class="record-message"><strong>${esc(e.service||'')}</strong><span>${esc(e.message||'')}</span><span>${esc(e.preference||'WhatsApp')} · ${esc(e.context||'website')}</span></div></td><td>${esc(fmt(e.createdAt))}</td><td><span class="status-pill status-${esc(e.status)}">${esc(e.status)}</span></td><td>${enquiryActions(e)}</td></tr>`).join('');cards.innerHTML=items.map(e=>`<article class="record-card"><div class="record-card-top"><div><h3>${esc(e.name)}</h3><small>${esc(e.phone)} · ${esc(e.service||'')}</small></div><span class="status-pill status-${esc(e.status)}">${esc(e.status)}</span></div><p>${esc(e.message||'')}</p><small>${esc(fmt(e.createdAt))}</small>${enquiryActions(e)}</article>`).join('');bindActions()}
function renderReviews(){const q=$('[data-review-search]')?.value||'',st=$('[data-review-filter]')?.value||'all',items=filterList(reviews,q,st,['name','service','message']);const tb=$('[data-review-table]'),cards=$('[data-review-cards]');if(!tb||!cards)return;if(!items.length){tb.innerHTML='<tr><td colspan="5" class="empty-state">No reviews found.</td></tr>';cards.innerHTML='<div class="empty-state">No reviews found.</div>';return}tb.innerHTML=items.map(r=>`<tr><td><div class="record-customer"><strong>${esc(r.name)}</strong><span>${esc(r.service||'')}</span><span>${'★'.repeat(Number(r.rating)||0)}</span></div></td><td><div class="record-message"><span>${esc(r.message||'')}</span></div></td><td>${esc(fmt(r.createdAt))}</td><td><span class="status-pill status-${esc(r.status)}">${esc(r.status)}</span></td><td>${reviewActions(r)}</td></tr>`).join('');cards.innerHTML=items.map(r=>`<article class="record-card"><div class="record-card-top"><div><h3>${esc(r.name)} · ${'★'.repeat(Number(r.rating)||0)}</h3><small>${esc(r.service||'')}</small></div><span class="status-pill status-${esc(r.status)}">${esc(r.status)}</span></div><p>${esc(r.message||'')}</p><small>${esc(fmt(r.createdAt))}</small>${reviewActions(r)}</article>`).join('');bindActions()}
function renderActivity(){const box=$('[data-activity-list]');if(!box)return;const items=[...enquiries.map(x=>({...x,_type:'Enquiry'})),...reviews.map(x=>({...x,_type:'Review'}))].sort((a,b)=>ms(b.createdAt)-ms(a.createdAt)).slice(0,8);box.innerHTML=items.length?items.map(x=>`<div class="activity-item"><div class="activity-icon">${x._type==='Review'?'R':'E'}</div><div><strong>${esc(x.name||'Unknown')} · ${esc(x._type)}</strong><small>${esc(x.service||'')} · ${esc(x.status||'')}</small></div><time>${esc(fmt(x.createdAt))}</time></div>`).join(''):'<div class="empty-state">No activity yet.</div>'}
async function updateDoc(coll,id,data){try{await fs.updateDoc(fs.doc(db,coll,id),data);toast('Updated successfully')}catch(e){console.error(e);toast('Update failed','error')}}
async function deleteDoc(coll,id){if(!confirm('Delete this record permanently?'))return;try{await fs.deleteDoc(fs.doc(db,coll,id));toast('Deleted')}catch(e){console.error(e);toast('Delete failed','error')}}
function bindActions(){
  $$('[data-e-status]').forEach(b=>b.onclick=()=>updateDoc('enquiries',b.dataset.id,{status:b.dataset.eStatus,updatedAt:fs.serverTimestamp()}));
  $$('[data-r-status]').forEach(b=>b.onclick=()=>updateDoc('reviews',b.dataset.id,{status:b.dataset.rStatus,updatedAt:fs.serverTimestamp()}));
  $$('[data-e-delete]').forEach(b=>b.onclick=()=>deleteDoc('enquiries',b.dataset.id));$$('[data-r-delete]').forEach(b=>b.onclick=()=>deleteDoc('reviews',b.dataset.id));
}
['[data-enquiry-search]','[data-enquiry-filter]'].forEach(s=>$(s)?.addEventListener('input',renderEnquiries));['[data-review-search]','[data-review-filter]'].forEach(s=>$(s)?.addEventListener('input',renderReviews));
$('[data-refresh]')?.addEventListener('click',()=>{renderAll();toast('Dashboard refreshed')});
$$('[data-admin-tab]').forEach(b=>b.addEventListener('click',()=>{const t=b.dataset.adminTab;$$('[data-admin-tab]').forEach(x=>x.classList.toggle('active',x===b));$$('[data-view]').forEach(v=>v.hidden=v.dataset.view!==t);$('[data-admin-title]').textContent=t[0].toUpperCase()+t.slice(1);$('.admin-sidebar')?.classList.remove('open')}));
$('[data-admin-nav-toggle]')?.addEventListener('click',()=>$('.admin-sidebar')?.classList.toggle('open'));
