# Buddy Computers

Complete English business website for Ahmedabad: Home, detailed Services, About us, Contact us, and custom 404. Dependency-free static HTML/CSS/JavaScript, with light/dark preferences, reduced-motion support and an accessible WhatsApp contact chooser.

## Deploy using GitHub and Vercel

1. Upload this folder's contents to a GitHub repository (keep `dist` and `vercel.json` at the repository root).
2. In Vercel, import that repository. Select **Other** as the framework.
3. Leave Build Command empty and set Output Directory to **dist**. No dependencies or environment variables are needed.
4. Deploy. Vercel provides an HTTPS address. GitHub changes trigger new deployments.

`dist/` is the ready-to-deploy website. `build.py` generates the HTML pages if copy changes are needed; Python 3 is needed only to regenerate pages, not to host them. Edit styling in `dist/assets/style.css` and interactions in `dist/assets/app.js`.

## After receiving the final public URL

Add a canonical URL for each page, create a sitemap.xml listing the four public pages and reference it in robots.txt. Submit the sitemap through Google Search Console. No domain has been invented in this package.

## Performance target

97+ in mobile and desktop Performance, Accessibility, Best Practices and SEO is the target, not a verified claim. Run PageSpeed Insights on the deployed HTTPS URL for every page, then address remaining findings. This version uses no third-party scripts, no web-font requests, small JavaScript, fixed image dimensions and reduced-motion support. The logo is the supplied image; the SVG favicon frames only its symbol and excludes the wordmark.

## Business facts

Ahmedabad-wide service by appointment. Home/office visits, remote assistance and repair/return where needed. Monday–Sunday, 10 AM–8 PM. No shop address, fixed prices, fabricated reviews, experience years, or unverified guarantees are included. WhatsApp links open a drafted enquiry; the visitor sends it themselves. Theme preference is stored only on the visitor's device.
