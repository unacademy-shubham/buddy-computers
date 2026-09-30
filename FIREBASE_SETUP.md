# Firebase setup for Buddy Computers

This website is already coded to use Firebase for:

- Website enquiries
- Customer review submissions
- Review approval / rejection
- Enquiry status management
- Secure admin login

## 1. Create the Firebase project

1. Open Firebase Console and create a project, for example **Buddy Computers**.
2. Add a **Web App** to the project.
3. Copy the Firebase web configuration values.
4. Open `dist/assets/firebase-config.js` and replace every `YOUR_...` placeholder with the copied values.

Firebase Web App config is designed to be visible in a website. Access to database records is controlled by Firestore Security Rules.

## 2. Enable Firestore

1. In Firebase Console, open **Firestore Database**.
2. Create the database.
3. Use the rules supplied in this ZIP: `firestore.rules`.

If Firebase CLI is installed, from the repository root you can deploy only the rules with:

```bash
firebase login
firebase use --add
firebase deploy --only firestore:rules
```

Or paste the contents of `firestore.rules` into Firestore > Rules in Firebase Console and publish them.

## 3. Enable admin login

1. Open **Authentication > Sign-in method**.
2. Enable **Email/Password**.
3. Open **Authentication > Users** and create this admin account:

`buddycomputersofficial@gmail.com`

Choose a strong password.

The included Firestore rules allow admin access only to this email. If you want to use a different admin email, change it in both:

- `dist/assets/firebase-config.js` (`BUDDY_ADMIN_EMAIL`)
- `firestore.rules` (`isAdmin()`)

Then publish the updated rules.

## 4. Test the flow

1. Deploy the site or run it locally through a web server.
2. Submit an enquiry from `/contact/`.
3. Submit a review from `/reviews/`.
4. Open `/admin/` and sign in.
5. Mark the enquiry as Contacted / Resolved.
6. Approve the review.
7. Reload `/reviews/` or the Home page. The approved review should appear publicly.

## 5. Vercel

This is a static website. In Vercel:

- Framework Preset: **Other**
- Build Command: leave empty
- Output Directory: `dist`

No Firebase secret key is needed in Vercel.

## Important security note

Do not change Firestore rules to `allow read, write: if true;`. The supplied rules intentionally allow public users to create only a restricted enquiry or pending review, while admin access requires Firebase Authentication.
