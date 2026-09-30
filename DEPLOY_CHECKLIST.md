# Launch checklist

1. Create Firebase project.
2. Copy web config into `dist/assets/firebase-config.js`.
3. Enable Firestore.
4. Publish `firestore.rules`.
5. Enable Email/Password Authentication.
6. Create admin user: `buddycomputersofficial@gmail.com`.
7. Push repository to GitHub.
8. Import repository in Vercel.
9. Framework: Other; Output Directory: `dist`.
10. Deploy and test:
   - Call links
   - Both WhatsApp contacts
   - Contact enquiry submission
   - Review submission
   - `/admin/` login
   - Enquiry status updates
   - Review approve/reject
   - Approved review appears publicly
11. Add the deployed URL to Google Search Console and submit `/sitemap.xml`.
12. When `buddycomputers.com` or `buddycomputers.in` is purchased, update `SITE_URL` in `build.py`, run `python3 build.py`, redeploy, and connect the custom domain in Vercel.

## Before launch, optional

If an Instagram account is ready, add its real link to the website. No placeholder Instagram handle has been invented in this build.
