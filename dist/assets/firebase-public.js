const cfg = window.BUDDY_FIREBASE_CONFIG || {};
export const firebaseConfigured = Boolean(cfg.apiKey && cfg.projectId && !String(cfg.apiKey).startsWith('YOUR_') && !String(cfg.projectId).startsWith('YOUR_'));
let sdkPromise;

async function sdk(){
  if (!firebaseConfigured) return null;
  if (!sdkPromise) sdkPromise = Promise.all([
    import('https://www.gstatic.com/firebasejs/11.10.0/firebase-app.js'),
    import('https://www.gstatic.com/firebasejs/11.10.0/firebase-firestore.js')
  ]).then(([appMod, fsMod])=>{
    const app = appMod.getApps().length ? appMod.getApp() : appMod.initializeApp(cfg);
    return { app, db: fsMod.getFirestore(app), fs: fsMod };
  });
  return sdkPromise;
}

export async function submitEnquiry(data){
  const x=await sdk(); if(!x) throw new Error('FIREBASE_NOT_CONFIGURED');
  const {addDoc,collection,serverTimestamp}=x.fs;
  return addDoc(collection(x.db,'enquiries'),{...data,status:'new',createdAt:serverTimestamp()});
}
export async function submitReview(data){
  const x=await sdk(); if(!x) throw new Error('FIREBASE_NOT_CONFIGURED');
  const {addDoc,collection,serverTimestamp}=x.fs;
  return addDoc(collection(x.db,'reviews'),{...data,status:'pending',createdAt:serverTimestamp()});
}
export async function getApprovedReviews(){
  const x=await sdk(); if(!x) return [];
  const {collection,getDocs,query,where}=x.fs;
  const snap=await getDocs(query(collection(x.db,'reviews'),where('status','==','approved')));
  return snap.docs.map(d=>({id:d.id,...d.data()})).sort((a,b)=>toMs(b.createdAt)-toMs(a.createdAt));
}
function toMs(v){ if(!v) return 0; if(typeof v.toMillis==='function') return v.toMillis(); if(v.seconds) return v.seconds*1000; return 0 }
