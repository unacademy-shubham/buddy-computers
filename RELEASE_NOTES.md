# Buddy Computers — Final Release Notes

## UX / visual fixes
- Replaced the old footer white logo box with the supplied transparent Buddy Computers logo.
- Fixed footer logo sizing/flow so the description and enquiry button never overlap the logo.
- Added cinematic hero motion video with a lightweight 8-second loop.
- Added scroll-linked hero zoom, parallax movement, progress indicator and motion-led section reveals.
- Added subtle pointer tilt only on selected cards for desktop pointer devices.
- Added reduced-motion fallback and no-JavaScript content visibility fallback.
- Kept animations practical and performance-conscious rather than adding heavy 3D dependencies.

## Functional checks performed
- Python build script completed successfully.
- JavaScript syntax checks passed for public and admin scripts.
- Python syntax check passed for build script.
- HTML/static asset/link checks passed across 8 generated HTML pages.
- Footer layout smoke test passed at desktop (1440px) and mobile (390px) widths with no horizontal overflow and no logo/paragraph/button overlap.
- Public enquiry/review/WhatsApp modal smoke tests passed with Firebase-unconfigured fallback behavior.
- Hero motion video verified with ffprobe: 8 seconds, ~190 KB, MP4/H.264.
- Vercel static route structure includes Home, Services, About, Contact, Reviews, Privacy, Admin and 404.

## Firebase
Firebase remains configuration-driven. Replace the placeholders in `dist/assets/firebase-config.js`, enable Firestore + Email/Password Authentication, and publish `firestore.rules` before using the live enquiry/review/admin features.
