# Buddy Computers — Website + Firebase Admin

Production-ready static website for Buddy Computers, Ahmedabad.

## Included

- Premium responsive Home page
- Detailed Services page
- About page
- Contact page with enquiry form
- Customer Reviews page
- Privacy page
- Custom 404
- Dark / light theme
- WhatsApp contact chooser (Navin first, Shubham second)
- Doorstep / home & office service messaging
- Firebase-backed enquiries and reviews
- `/admin/` dashboard for enquiry handling and review moderation
- SEO metadata, Open Graph image, Schema.org markup, sitemap and robots.txt
- New supplied Buddy Computers logo with transparent background
- GitHub + Vercel-ready static deployment

## Business model reflected in the website

Buddy Computers has no public physical shop. Customers connect through the website, phone or WhatsApp. Service is arranged at the customer's home or workplace across Ahmedabad. If detailed repair is required, a system can be collected and returned after the work is completed.

## Contacts

1. Navin Sharma — 70963 10195
2. Shubham Jangir — 74269 33642

Both are displayed side-by-side where practical, with Navin on the left / first and Shubham on the right / second.

## Deploy to Vercel

1. Push the contents of this folder to GitHub.
2. Import the repository into Vercel.
3. Framework: **Other**.
4. Build Command: leave empty.
5. Output Directory: `dist`.
6. Deploy.

## Firebase

The website works for calls and WhatsApp before Firebase is connected. The database forms and admin panel require Firebase setup.

Follow **FIREBASE_SETUP.md**.

## Domain

The current SEO base URL is `https://buddycomputers.vercel.app`.

When you buy `buddycomputers.com` or `buddycomputers.in`, update `SITE_URL` near the top of `build.py`, run:

```bash
python3 build.py
```

Then redeploy. This regenerates canonical URLs, Open Graph URLs, sitemap and robots.txt.

## Editing website content

Most public page content is maintained in `build.py`.

After changing text in `build.py`, run:

```bash
python3 build.py
```

Styles: `dist/assets/style.css`

Public interactions: `dist/assets/app.js`

Admin styling: `dist/assets/admin.css`

Admin logic: `dist/assets/admin.js`

Firebase config: `dist/assets/firebase-config.js`
