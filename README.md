# Buddy Computers — Cinematic Website + Firebase Admin

High-end, practical website for Buddy Computers, Ahmedabad. The public experience uses a lightweight cinematic hero video, scroll-linked zoom/parallax, reveal transitions, subtle card tilt and responsive motion—without requiring a heavy animation framework.

## Included

- Cinematic full-screen hero with looping motion background
- Scroll-linked hero zoom and progress indicator
- Smooth, premium reveal transitions
- Subtle pointer tilt on selected cards
- Responsive mobile/tablet/desktop layouts
- Detailed Services, About, Contact and Reviews pages
- Customer enquiry form
- Customer review submission with moderation
- Firebase Firestore for enquiries/reviews
- Firebase Authentication admin login
- `/admin/` dashboard for enquiry status and review approval
- Dark / light theme
- WhatsApp contact chooser
- Navin Sharma first/left and Shubham Jangir second/right
- Transparent supplied Buddy Computers logo
- SEO metadata, Open Graph, Schema.org, sitemap, robots.txt and 404
- GitHub + Vercel-ready static deployment

## Business model

Buddy Computers has no public physical shop. Customers connect through the website, phone or WhatsApp. Service is arranged at the customer's home or workplace across Ahmedabad. If detailed repair is required, a system can be collected and returned after the work is completed.

## Contacts

1. Navin Sharma — 70963 10195
2. Shubham Jangir — 74269 33642

## Deploy to Vercel

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Framework Preset: **Other**.
4. Build Command: leave empty.
5. Output Directory: `dist`.
6. Deploy.

## Firebase

Follow `FIREBASE_SETUP.md` to create the Firebase project, enable Firestore and Email/Password Authentication, configure `dist/assets/firebase-config.js`, and publish `firestore.rules`.

Before Firebase is configured, the site still provides direct call/WhatsApp contact. Enquiry and review database features become active after Firebase is connected.

## Domain

The temporary SEO base URL is `https://buddycomputers.vercel.app`. When `buddycomputers.com` or `buddycomputers.in` is purchased, update `SITE_URL` near the top of `build.py`, run `python3 build.py`, and redeploy.

## Editing

Most public page content is in `build.py`. Styles are in `dist/assets/style.css`; public interactions are in `dist/assets/app.js`; admin logic/styling are in `dist/assets/admin.js` and `dist/assets/admin.css`.
