from pathlib import Path
import json

ROOT = Path(__file__).parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)

SITE_URL = 'https://buddycomputers.vercel.app'
EMAIL = 'buddycomputersofficial@gmail.com'
CONTACTS = [
    ('Navin Sharma', '+917096310195', '70963 10195'),
    ('Shubham Jangir', '+917426933642', '74269 33642'),
]

SERVICES = [
    {
        'slug':'repair','num':'01','title':'PC & laptop repair','short':'Diagnosis and repair for startup, hardware, overheating and performance problems.',
        'icon':'wrench',
        'items':[
            ('Startup & stability','No power, black screens, Windows boot failures, blue-screen errors, unexpected restarts, freezing and application crashes. We diagnose whether the issue is hardware, drivers or software.'),
            ('Hardware diagnosis & repair','Motherboard and power-related faults, RAM errors, failing HDDs and SSDs, laptop charging problems, keyboard and display issues, damaged ports, fans and connected components.'),
            ('Cooling & preventive servicing','Internal dust cleaning, thermal paste replacement, cooling fan checks and overheating troubleshooting.'),
            ('Performance troubleshooting','Slow startup, high CPU or memory usage, low storage and background software issues. We identify the bottleneck before recommending an upgrade.'),
        ]
    },
    {
        'slug':'software','num':'02','title':'Windows, software & data','short':'Windows setup, software troubleshooting, malware cleanup, backups and migration.',
        'icon':'window',
        'items':[
            ('Windows installation & formatting','Fresh installation, reinstallation, formatting, boot repair, Windows update troubleshooting and essential driver setup. We discuss your files before any formatting.'),
            ('Software & driver support','Installation and configuration of properly licensed software, application errors, driver conflicts and compatibility problems.'),
            ('Virus & security support','Malware and unwanted software removal, browser pop-up troubleshooting, antivirus configuration and practical security settings.'),
            ('Backup, migration & account recovery','File backup and transfer, SSD migration and owner-authorised Windows password reset or account recovery. Recovery depends on drive condition, encryption and the issue involved.'),
        ]
    },
    {
        'slug':'builds','num':'03','title':'Custom PC builds & upgrades','short':'Balanced systems and compatible upgrades for home, office, gaming and creative work.',
        'icon':'cpu',
        'items':[
            ('Custom PC assembly','Requirement-based component selection and assembly for home, office, gaming, design, video editing and professional workloads.'),
            ('SSD, RAM & storage upgrades','Memory expansion, SSD installation, additional storage and data migration where supported. Compatibility is checked before parts are recommended.'),
            ('CPU, graphics & power upgrades','Compatible processor, graphics card, power supply and cooling upgrades with attention to power requirements, clearance and system balance.'),
            ('Setup & handover','Operating system and driver configuration, peripheral setup and an explanation of the completed work.'),
        ]
    },
    {
        'slug':'networking','num':'04','title':'Networking & IT support','short':'Home and office networks, Wi-Fi, routers, switches and practical IT support.',
        'icon':'network',
        'items':[
            ('Office LAN & WLAN setup','Wired office networks, wireless network planning, access point setup and Wi-Fi coverage troubleshooting for homes and businesses.'),
            ('Routers, switches & VLANs','Router and switch configuration, IP addressing, DHCP setup, VLAN segmentation and device connectivity troubleshooting.'),
            ('Firewall configuration','Firewall rules and access settings based on your requirements, plus authorised connectivity troubleshooting.'),
            ('On-site & remote IT support','Computer and software troubleshooting at your home or office, remote assistance when suitable, printer/scanner setup and peripheral support.'),
        ]
    },
    {
        'slug':'websites','num':'05','title':'Website development','short':'Responsive business websites designed to explain, build trust and convert visitors into enquiries.',
        'icon':'code',
        'items':[
            ('Business & portfolio websites','Responsive websites that explain your services clearly and guide visitors towards a useful action such as a call, WhatsApp message or enquiry.'),
            ('Redesign & maintenance','Content and layout updates, mobile usability improvements, broken page fixes and ongoing website maintenance.'),
            ('Performance & accessibility','Attention to loading speed, readable content, keyboard navigation, image optimisation and search-friendly structure.'),
            ('Launch support','Domain and hosting setup assistance, deployment and basic handover. The platform and scope are selected around the project.'),
        ]
    },
    {
        'slug':'creative','num':'06','title':'Logo design & video editing','short':'Brand visuals, social creatives and edited video content for businesses and creators.',
        'icon':'spark',
        'items':[
            ('Logo design','Business logo concepts and refinements shaped around your brand, audience and intended use.'),
            ('Video editing','Editing for business videos, reels and promotional content, including cuts, transitions, captions, audio adjustments and export formatting.'),
            ('Social media creatives','Branded promotional graphics and social designs with sizes and deliverables agreed for the project.'),
        ]
    },
    {
        'slug':'seo','num':'07','title':'SEO & Google Business','short':'Search-friendly pages, indexing setup and Google Business Profile assistance.',
        'icon':'search',
        'items':[
            ('On-page & technical SEO','Page titles, descriptions, heading structure, internal links and technical checks that help search engines understand your website.'),
            ('Search Console & indexing','Google Search Console setup, sitemap submission and diagnosis of indexing issues. Indexing decisions and timing are controlled by Google.'),
            ('Google Business Profile','Profile creation and setup, support with verification, services, contact details and opening hours, subject to Google eligibility requirements.'),
            ('Local search foundations','Improve the consistency and relevance of your business information for local searches. Search positions and verification outcomes are not guaranteed.'),
        ]
    },
]

ICONS = {
'wrench':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.7 6.3a4.5 4.5 0 0 0-5.9 5.9L3.5 17.5a2.1 2.1 0 1 0 3 3l5.3-5.3a4.5 4.5 0 0 0 5.9-5.9l-2.8 2.8-3-3 2.8-2.8Z"/></svg>',
'window':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/></svg>',
'cpu':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3M10 10h4v4h-4z"/></svg>',
'network':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="2" width="8" height="5" rx="1"/><rect x="2" y="17" width="8" height="5" rx="1"/><rect x="14" y="17" width="8" height="5" rx="1"/><path d="M12 7v5M6 17v-5h12v5"/></svg>',
'code':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 9-4 3 4 3M16 9l4 3-4 3M14 5l-4 14"/></svg>',
'spark':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 1.5 5.1L18 9l-4.5 1.9L12 16l-1.5-5.1L6 9l4.5-1.9L12 2ZM5 15l.8 2.2L8 18l-2.2.8L5 21l-.8-2.2L2 18l2.2-.8L5 15ZM19 14l.8 2.2L22 17l-2.2.8L19 20l-.8-2.2L16 17l2.2-.8L19 14Z"/></svg>',
'search':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M11 8v6M8 11h6"/></svg>',
'home':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m3 11 9-8 9 8v10h-7v-6h-4v6H3V11Z"/></svg>',
'pickup':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v10H3zM14 10h4l3 3v4h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
'shield':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 5 6v5c0 4.7 2.9 8.1 7 10 4.1-1.9 7-5.3 7-10V6l-7-3Z"/><path d="m9 12 2 2 4-5"/></svg>',
'quote':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H8l-4 4V5Z"/><path d="M8 9h8M8 12h5"/></svg>',
}

def nav(active=''):
    items=[('home','/','Home'),('services','/services/','Services'),('about','/about/','About'),('reviews','/reviews/','Reviews'),('contact','/contact/','Contact')]
    return ''.join(f'<a href="{href}" {"aria-current=page" if key==active else ""}>{label}</a>' for key,href,label in items)

def button(label, href=None, kind='primary', attrs=''):
    if href:
        return f'<a class="btn {kind}" href="{href}" {attrs}>{label}<span aria-hidden="true">↗</span></a>'
    return f'<button class="btn {kind}" {attrs}>{label}<span aria-hidden="true">↗</span></button>'

def shell(active, title, desc, body, path='/', noindex=False, extra_head='', scripts=''):
    canonical = SITE_URL.rstrip('/') + path
    schema = {
        '@context':'https://schema.org',
        '@type':'ProfessionalService',
        'name':'Buddy Computers',
        'url':SITE_URL,
        'image':SITE_URL+'/assets/og-image.jpg',
        'description':'Doorstep computer repair, IT support, networking and digital services across Ahmedabad.',
        'email':EMAIL,
        'telephone':[c[1] for c in CONTACTS],
        'areaServed':{'@type':'City','name':'Ahmedabad'},
        'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],'opens':'10:00','closes':'20:00'}],
        'sameAs':[]
    }
    robots = '<meta name="robots" content="noindex,nofollow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Buddy Computers">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE_URL}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE_URL}/assets/og-image.jpg">
<meta name="theme-color" content="#f7fbff">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-192.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<script src="/assets/theme.js"></script>
<script src="/assets/firebase-config.js"></script>
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(schema)}</script>
{extra_head}
<script defer src="/assets/app.js"></script>{scripts}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header" data-header>
  <div class="container header-inner">
    <a class="brand" href="/" aria-label="Buddy Computers home"><img src="/assets/buddy-symbol.png" width="512" height="512" alt="" decoding="async"><span class="brand-wordmark"><b>Buddy</b><i>Computers</i></span></a>
    <nav class="desktop-nav" aria-label="Primary">{nav(active)}</nav>
    <div class="header-actions">
      <button class="icon-btn" type="button" data-theme-toggle aria-label="Switch color theme"><span class="theme-icon" aria-hidden="true">◐</span></button>
      <button class="menu-btn" type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span><span class="sr-only">Menu</span></button>
      <button class="btn compact primary desktop-cta" type="button" data-enquiry-open>Book a service <span aria-hidden="true">↗</span></button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu" data-mobile-menu>
    <nav aria-label="Mobile">{nav(active)}</nav>
    <div class="mobile-menu-cta"><button class="btn primary full" type="button" data-enquiry-open>Book a service <span aria-hidden="true">↗</span></button></div>
  </div>
</header>
<main id="main">{body}</main>
<footer class="site-footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <div class="footer-logo-wrap"><img src="/assets/buddy-logo.webp" alt="Buddy Computers" width="1100" height="856" loading="lazy"></div>
      <p>Doorstep computer, IT and digital support across Ahmedabad.</p>
      <button class="btn light" type="button" data-enquiry-open>Start an enquiry <span aria-hidden="true">↗</span></button>
    </div>
    <div class="footer-col"><h2>Explore</h2>{nav(active)}</div>
    <div class="footer-col"><h2>Services</h2><a href="/services/#repair">Computer repair</a><a href="/services/#builds">PC builds & upgrades</a><a href="/services/#networking">Networking & IT</a><a href="/services/#websites">Web & digital</a></div>
    <div class="footer-col"><h2>Contact</h2><a href="tel:+917096310195">Navin · 70963 10195</a><a href="tel:+917426933642">Shubham · 74269 33642</a><a href="mailto:{EMAIL}">{EMAIL}</a><span>Mon–Sun · 10 AM–8 PM</span></div>
  </div>
  <div class="container footer-contacts" aria-label="Phone contacts">
    <a href="tel:+917096310195"><small>Navin Sharma</small><strong>70963 10195</strong><span>Call ↗</span></a>
    <a href="tel:+917426933642"><small>Shubham Jangir</small><strong>74269 33642</strong><span>Call ↗</span></a>
  </div>
  <div class="container footer-bottom"><span>© 2026 Buddy Computers · Ahmedabad, India</span><div><a href="/privacy/">Privacy</a><a href="/admin/" rel="nofollow">Admin</a></div></div>
</footer>
<button class="floating-whatsapp" type="button" data-whatsapp-open aria-label="Contact Buddy Computers on WhatsApp"><span class="wa-dot" aria-hidden="true">●</span><span>WhatsApp</span></button>
<dialog class="contact-modal" id="contact-modal" data-contact-modal>
  <div class="modal-head"><div><span class="kicker">CHOOSE A CONTACT</span><h2>Talk to your buddy.</h2></div><button class="modal-close" type="button" data-modal-close aria-label="Close">×</button></div>
  <p data-modal-copy>Choose who you want to contact on WhatsApp.</p>
  <div class="contact-options">
    <a data-wa-navin href="https://wa.me/917096310195" target="_blank" rel="noopener"><span><strong>Navin Sharma</strong><small>70963 10195</small></span><b>WhatsApp ↗</b></a>
    <a data-wa-shubham href="https://wa.me/917426933642" target="_blank" rel="noopener"><span><strong>Shubham Jangir</strong><small>74269 33642</small></span><b>WhatsApp ↗</b></a>
  </div>
</dialog>
<dialog class="enquiry-modal" id="enquiry-modal" data-enquiry-modal>
  <div class="modal-head"><div><span class="kicker">QUICK ENQUIRY</span><h2>Tell us what you need.</h2></div><button class="modal-close" type="button" data-enquiry-close aria-label="Close">×</button></div>
  <form class="form-stack" data-enquiry-form data-context="quick enquiry">
    <div class="field-row"><label><span>Name *</span><input name="name" autocomplete="name" required maxlength="80" placeholder="Your name"></label><label><span>Phone *</span><input name="phone" inputmode="tel" autocomplete="tel" required maxlength="20" placeholder="10-digit mobile number"></label></div>
    <label><span>Service *</span><select name="service" required><option value="">Choose a service</option>{''.join(f'<option>{s["title"]}</option>' for s in SERVICES)}<option>Other / not sure</option></select></label>
    <label><span>What can we help with? *</span><textarea name="message" required maxlength="1600" rows="4" placeholder="Device, issue, or project requirement"></textarea></label>
    <label class="honeypot" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>
    <div class="form-actions"><button class="btn primary" type="submit">Send enquiry <span aria-hidden="true">↗</span></button><small>We’ll use these details only to respond to your enquiry.</small></div>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</dialog>
</body></html>'''

def page_intro(kicker, title, copy, actions=''):
    return f'''<section class="page-hero"><div class="container page-hero-grid"><div><span class="kicker">{kicker}</span><h1>{title}</h1></div><div><p class="lead">{copy}</p>{actions}</div></div></section>'''

# HOME
service_cards=''.join(f'''<a class="service-card" href="/services/#{s['slug']}"><div class="service-card-top"><span class="service-icon">{ICONS[s['icon']]}</span><span class="service-num">{s['num']}</span></div><h3>{s['title']}</h3><p>{s['short']}</p><span class="text-link">Explore service <b>↗</b></span></a>''' for s in SERVICES)

home = f'''
<section class="home-hero">
  <div class="container hero-grid">
    <div class="hero-copy reveal">
      <div class="hero-pill"><span></span> Doorstep computer & IT service · Ahmedabad</div>
      <h1>Computer trouble?<br><em>We come to you.</em></h1>
      <p class="hero-lead">PC and laptop repair, upgrades, office networking and digital support—at your home or workplace. If the job needs more work, we arrange pickup, repair and return.</p>
      <div class="hero-actions">{button('Book a doorstep visit', None, 'primary', 'type="button" data-enquiry-open')} {button('Explore services','/services/','secondary')}</div>
      <div class="hero-trust"><span>{ICONS['home']} Home & office visits</span><span>{ICONS['pickup']} Pickup & return when needed</span><span>{ICONS['quote']} Quote before work</span></div>
    </div>
    <div class="hero-visual reveal" data-delay="1">
      <div class="hero-image-shell"><picture><source srcset="/assets/pc-hero.webp" type="image/webp"><img src="/assets/pc-hero.jpg" width="800" height="600" alt="Custom desktop computer with illuminated internal components" fetchpriority="high"></picture><div class="hero-shade"></div></div>
      <div class="hero-float card-a"><span class="mini-icon">{ICONS['wrench']}</span><div><small>Computer care</small><strong>Repair · Upgrade</strong></div></div>
      <div class="hero-float card-b"><span class="mini-icon green">{ICONS['network']}</span><div><small>Business support</small><strong>IT · Network · Web</strong></div></div>
      <div class="hero-brand-mark"><img src="/assets/buddy-symbol.png" alt="" width="512" height="512"></div>
    </div>
  </div>
</section>
<section class="promise-bar"><div class="container"><span>No shop visit needed</span><i></i><span>Appointment-based service</span><i></i><span>All Ahmedabad</span><i></i><span>7 days a week</span></div></section>
<section class="section container" id="services">
  <div class="section-head"><div><span class="kicker">WHAT WE DO</span><h2>One tech partner.<br><span>Seven ways to help.</span></h2></div><p>From a laptop that won’t boot to a business that needs a stronger digital presence, choose the support that fits.</p></div>
  <div class="service-grid">{service_cards}</div>
</section>
<section class="section dark-section">
  <div class="container"><div class="section-head light"><div><span class="kicker">HOW IT WORKS</span><h2>From first message<br><span>to problem solved.</span></h2></div><p>Simple communication, clear next steps and service that works around the job—not around a shop counter.</p></div>
    <div class="steps-grid">
      <article><span>01</span><div class="step-icon">{ICONS['quote']}</div><h3>Tell us the problem</h3><p>Call, WhatsApp or send an enquiry with your device issue or project requirement.</p></article>
      <article><span>02</span><div class="step-icon">{ICONS['home']}</div><h3>We visit & diagnose</h3><p>We come to your home or workplace by appointment and assess what the job needs.</p></article>
      <article><span>03</span><div class="step-icon">{ICONS['wrench']}</div><h3>Fix on-site when possible</h3><p>If it can be completed safely on-site, we do the work there after discussing the quote.</p></article>
      <article><span>04</span><div class="step-icon">{ICONS['pickup']}</div><h3>Pickup when required</h3><p>For workshop-level work, we arrange pickup and return after the repair is completed.</p></article>
    </div>
  </div>
</section>
<section class="section container why-section">
  <div class="section-head"><div><span class="kicker">WHY BUDDY COMPUTERS</span><h2>Useful support.<br><span>Without the runaround.</span></h2></div><p>We’re building Buddy Computers around a straightforward idea: make technical help easier to access and easier to understand.</p></div>
  <div class="value-grid"><article><span>{ICONS['home']}</span><h3>We come to you</h3><p>No shop visit required. Service is arranged at your home or workplace across Ahmedabad.</p></article><article><span>{ICONS['shield']}</span><h3>Data-aware process</h3><p>Important files and backup options are discussed before formatting or other data-sensitive work.</p></article><article><span>{ICONS['quote']}</span><h3>Work discussed first</h3><p>The requirement, next step and expected work are discussed before proceeding.</p></article><article><span>{ICONS['code']}</span><h3>Hardware to digital</h3><p>Computer repair, networks, websites and digital services—one point of contact for practical technology needs.</p></article></div>
</section>
<section class="section reviews-preview" data-reviews-section>
  <div class="container"><div class="section-head"><div><span class="kicker">CUSTOMER REVIEWS</span><h2>Built on real<br><span>customer experiences.</span></h2></div><div><p>No made-up testimonials. Reviews shown here are submitted by customers and approved before they appear publicly.</p><a class="text-link large" href="/reviews/">Read or leave a review <b>↗</b></a></div></div>
  <div class="review-grid" data-approved-reviews data-limit="3"><article class="review-empty"><div class="stars">★★★★★</div><h3>We’re just getting started.</h3><p>Be among our first customers and share your experience after your service.</p><a class="btn secondary" href="/reviews/#leave-review">Leave a review <span>↗</span></a></article></div></div>
</section>
<section class="section container portfolio-section">
  <div class="portfolio-copy"><span class="kicker">OUR DIGITAL WORK</span><h2>Meet <span>Buddy Fleets.</span></h2><p class="lead">A fleet-management website and platform project built with the same practical approach we bring to every technology problem.</p><a class="btn secondary" href="https://buddyfleets.in" target="_blank" rel="noopener">Visit Buddy Fleets <span>↗</span></a></div>
  <a class="portfolio-card" href="https://buddyfleets.in" target="_blank" rel="noopener"><div class="portfolio-grid-lines"></div><span>WEBSITE DEVELOPMENT / PORTFOLIO</span><strong>Buddy Fleets<i>.</i></strong><p>Fleet intelligence.<br>Built for the road ahead.</p><small>buddyfleets.in ↗</small></a>
</section>
<section class="cta-band"><div class="container cta-band-grid"><div><span class="kicker">NEED HELP TODAY?</span><h2>Tell us what’s not working.</h2><p>We’ll help you work out the next practical step.</p></div><div class="cta-actions"><button class="btn light" type="button" data-enquiry-open>Book a service <span>↗</span></button><button class="btn outline-light" type="button" data-whatsapp-open>WhatsApp us <span>↗</span></button></div></div></section>
'''

# SERVICES
service_sections=''
for s in SERVICES:
    items=''.join(f'<article><span>{i:02d}</span><div><h3>{h}</h3><p>{d}</p></div></article>' for i,(h,d) in enumerate(s['items'],1))
    service_sections += f'''<section class="service-detail" id="{s['slug']}"><div class="service-detail-side"><span class="service-icon big">{ICONS[s['icon']]}</span><span class="service-num">{s['num']}</span><h2>{s['title']}</h2><p>{s['short']}</p><button class="btn secondary" type="button" data-enquiry-open data-service="{s['title']}">Ask about this service <span>↗</span></button></div><div class="service-detail-list">{items}</div></section>'''
services_page = page_intro('SERVICES','Practical support.<br><span>For real technology needs.</span>','Computer repair, upgrades, networking and digital services for homes and businesses across Ahmedabad.',button('Book a service',None,'primary','type="button" data-enquiry-open')) + f'''<section class="container service-jump-wrap"><div class="service-jumps">{''.join(f'<a href="#{s["slug"]}">{s["num"]} · {s["title"]}</a>' for s in SERVICES)}</div>{service_sections}</section><section class="container data-care"><div class="data-care-icon">{ICONS['shield']}</div><div><span class="kicker">DATA CARE</span><h2>Your files matter.</h2><p>Tell us about important data before repair. We discuss backup options and get your approval before formatting or other work that could affect your files. Recovery may be limited by drive condition, encryption or the type of failure.</p></div></section><section class="cta-band"><div class="container cta-band-grid"><div><span class="kicker">NOT SURE WHICH SERVICE?</span><h2>Describe the issue. We’ll point you in the right direction.</h2></div><div class="cta-actions"><button class="btn light" type="button" data-enquiry-open>Start an enquiry <span>↗</span></button></div></div></section>'''

# ABOUT
about = page_intro('ABOUT BUDDY COMPUTERS','Technology help<br><span>that comes to you.</span>','Buddy Computers is an appointment-based computer, IT and digital service for customers across Ahmedabad.') + f'''
<section class="section container story-grid"><div><span class="kicker">OUR APPROACH</span><h2>Understand the problem.<br><span>Make the solution useful.</span></h2></div><div class="story-copy"><p>Buddy Computers is built around a simple idea: technical help should be practical, clear and easy to access.</p><p>Instead of asking customers to find a shop and carry their system across the city, we arrange service at your home or workplace. If a device needs workshop-level work, we can arrange collection and return after the requirement is discussed.</p><p>Our work covers PC and laptop problems, custom builds and upgrades, office networking, website development and digital support. The common thread is the same—understand what you actually need before recommending what to do next.</p></div></section>
<section class="section soft-section"><div class="container"><div class="section-head"><div><span class="kicker">HOW THE BUSINESS WORKS</span><h2>No storefront.<br><span>More convenient service.</span></h2></div><p>Buddy Computers operates online and by appointment. Customers connect through the website, phone or WhatsApp, and service is arranged around the job.</p></div><div class="model-grid"><article><span>01</span><h3>Connect online or by phone</h3><p>Send the problem, device details or project requirement.</p></article><article><span>02</span><h3>Site visit in Ahmedabad</h3><p>We arrange a suitable visit to your home or workplace.</p></article><article><span>03</span><h3>Repair, support or pickup</h3><p>Work is completed on-site when suitable, or the system is collected if more detailed repair is needed.</p></article><article><span>04</span><h3>Return & handover</h3><p>For collected systems, the completed device is returned and the work is explained.</p></article></div></div></section>
<section class="section container"><div class="section-head"><div><span class="kicker">THE PEOPLE BEHIND BUDDY COMPUTERS</span><h2>Two contacts.<br><span>One team.</span></h2></div><p>Reach either of us directly. Navin is shown first across the website, followed by Shubham.</p></div><div class="team-grid"><article class="person-card"><div class="person-avatar green">NS</div><div><small>OPERATIONS & CLIENT COORDINATION</small><h3>Navin Sharma</h3><p>Focused on customer requirements, coordinating service and keeping communication straightforward from first contact to completion.</p><div class="person-actions"><a href="tel:+917096310195">Call 70963 10195 ↗</a><a href="https://wa.me/917096310195?text=Hi%20Navin%2C%20I%20need%20help%20from%20Buddy%20Computers." target="_blank" rel="noopener">WhatsApp ↗</a></div></div></article><article class="person-card"><div class="person-avatar blue">SJ</div><div><small>TECHNOLOGY & DEVELOPMENT</small><h3>Shubham Jangir</h3><p>Focused on technical solutions, computer and IT support, website development and turning practical technology ideas into working systems.</p><div class="person-actions"><a href="tel:+917426933642">Call 74269 33642 ↗</a><a href="https://wa.me/917426933642?text=Hi%20Shubham%2C%20I%20need%20help%20from%20Buddy%20Computers." target="_blank" rel="noopener">WhatsApp ↗</a></div></div></article></div></section>
<section class="section dark-section"><div class="container"><div class="section-head light"><div><span class="kicker">WHAT MATTERS TO US</span><h2>Clear work.<br><span>Careful decisions.</span></h2></div></div><div class="value-grid dark"><article><span>{ICONS['quote']}</span><h3>Clear communication</h3><p>We explain the issue, discuss the required work and quote according to the task.</p></article><article><span>{ICONS['shield']}</span><h3>Data awareness</h3><p>Backup options and data-sensitive work are discussed before proceeding.</p></article><article><span>{ICONS['home']}</span><h3>Convenient support</h3><p>Home visits, office support, remote help or pickup and return—based on what the job needs.</p></article><article><span>{ICONS['search']}</span><h3>No invented claims</h3><p>We don’t publish fabricated reviews, made-up guarantees or experience numbers just to look bigger.</p></article></div></div></section>
'''

# CONTACT
contact = page_intro('CONTACT','Tell us the issue.<br><span>We’ll take it from there.</span>','Call, WhatsApp or send an enquiry. Service is available across Ahmedabad by appointment.') + f'''
<section class="section container contact-grid"><div class="contact-cards"><span class="kicker">CALL OR WHATSAPP</span><h2>Talk to your buddy.</h2><div class="contact-pair"><article><small>FIRST CONTACT</small><h3>Navin Sharma</h3><a class="big-phone" href="tel:+917096310195">70963 10195</a><div><a href="tel:+917096310195">Call now ↗</a><a href="https://wa.me/917096310195?text=Hi%20Navin%2C%20I%20need%20help%20from%20Buddy%20Computers." target="_blank" rel="noopener">WhatsApp ↗</a></div></article><article><small>SECOND CONTACT</small><h3>Shubham Jangir</h3><a class="big-phone" href="tel:+917426933642">74269 33642</a><div><a href="tel:+917426933642">Call now ↗</a><a href="https://wa.me/917426933642?text=Hi%20Shubham%2C%20I%20need%20help%20from%20Buddy%20Computers." target="_blank" rel="noopener">WhatsApp ↗</a></div></article></div><div class="contact-meta"><div><span>Service area</span><strong>All Ahmedabad</strong></div><div><span>Hours</span><strong>Mon–Sun · 10 AM–8 PM</strong></div><div><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><span>Service model</span><strong>Home / office visit · pickup if needed</strong></div></div></div>
<div class="form-card"><span class="kicker">ONLINE ENQUIRY</span><h2>Send the details.</h2><p>Share enough information for us to understand the request. Don’t include passwords or other sensitive credentials.</p><form class="form-stack" data-enquiry-form data-context="contact page"><div class="field-row"><label><span>Name *</span><input name="name" autocomplete="name" required maxlength="80" placeholder="Your name"></label><label><span>Phone *</span><input name="phone" inputmode="tel" autocomplete="tel" required maxlength="20" placeholder="Mobile number"></label></div><label><span>Email</span><input name="email" type="email" autocomplete="email" maxlength="120" placeholder="Optional"></label><label><span>Service *</span><select name="service" required><option value="">Choose a service</option>{''.join(f'<option>{s["title"]}</option>' for s in SERVICES)}<option>Other / not sure</option></select></label><label><span>Preferred contact</span><select name="preference"><option>WhatsApp</option><option>Phone call</option><option>Email</option></select></label><label><span>Tell us what you need *</span><textarea name="message" required maxlength="1600" rows="6" placeholder="Device model, symptoms, location area, or project requirement"></textarea></label><label class="honeypot" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label><button class="btn primary" type="submit">Submit enquiry <span>↗</span></button><p class="form-status" role="status" aria-live="polite"></p></form></div></section>
<section class="container faq-section"><div><span class="kicker">QUICK ANSWERS</span><h2>Before you book.</h2></div><div class="faq-list"><details><summary>Do you have a physical shop?</summary><p>No. Buddy Computers is an online, appointment-based service. We visit customers at their home or workplace across Ahmedabad.</p></details><details><summary>What if the computer cannot be repaired on-site?</summary><p>If the job needs more detailed work, we can discuss collection of the system, complete the repair and return it after the work is finished.</p></details><details><summary>Do you charge the same price for every repair?</summary><p>No fixed price list is published because the work depends on the device, fault and parts required. The next step and quote are discussed according to the job.</p></details><details><summary>Can you help businesses as well as home users?</summary><p>Yes. Services include PC support, office networking, routers and switches, Wi-Fi, websites and other digital requirements.</p></details><details><summary>What should I send in my first message?</summary><p>For a repair, share the device model, symptoms, your Ahmedabad area and whether important data is stored on the system. For digital work, share your goal, scope and timeline.</p></details></div></section>
'''

# REVIEWS
reviews = page_intro('REVIEWS','Real feedback.<br><span>Nothing fabricated.</span>','Customer reviews are submitted through this website and only appear publicly after approval.') + f'''
<section class="section container reviews-page-grid"><div><span class="kicker">APPROVED REVIEWS</span><h2>What customers say.</h2><div class="review-grid stacked" data-approved-reviews><article class="review-empty"><div class="stars">★★★★★</div><h3>No approved reviews yet.</h3><p>Buddy Computers is launching now. Genuine customer reviews will appear here after they are submitted and approved.</p></article></div></div><div class="form-card sticky" id="leave-review"><span class="kicker">SHARE YOUR EXPERIENCE</span><h2>Leave a review.</h2><p>Your review is sent to our admin panel as <strong>Pending</strong>. It becomes public only after approval.</p><form class="form-stack" data-review-form><label><span>Your name *</span><input name="name" autocomplete="name" required maxlength="80" placeholder="Your name"></label><label><span>Service used *</span><select name="service" required><option value="">Choose a service</option>{''.join(f'<option>{s["title"]}</option>' for s in SERVICES)}<option>Other</option></select></label><fieldset class="rating-field"><legend>Rating *</legend><div class="rating-picker">{''.join(f'<label><input type="radio" name="rating" value="{n}" {"required" if n==5 else ""}><span>{n}★</span></label>' for n in range(5,0,-1))}</div></fieldset><label><span>Your review *</span><textarea name="message" required maxlength="1000" rows="6" placeholder="How was your experience?"></textarea></label><label class="honeypot" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label><button class="btn primary" type="submit">Submit review <span>↗</span></button><p class="form-status" role="status" aria-live="polite"></p></form></div></section>
'''

privacy = page_intro('PRIVACY','Simple, clear<br><span>privacy information.</span>','This page explains what Buddy Computers collects through this website and why.') + '''<section class="section container prose"><h2>Information you choose to send</h2><p>When you submit an enquiry, we may collect your name, phone number, optional email address, selected service, contact preference and the message you send. When you submit a review, we may collect your name, service, rating and review text.</p><h2>How we use it</h2><p>Enquiry information is used to understand your request, contact you and manage the service conversation. Review information is used to moderate and, if approved, display genuine customer feedback on the website.</p><h2>Review moderation</h2><p>Submitted reviews start as pending. Buddy Computers may approve, reject or remove a review. We do not intentionally publish phone numbers, email addresses or passwords as part of a review.</p><h2>Website storage</h2><p>The website may store a color-theme preference in your browser. Enquiries, reviews and administrator access use Firebase when Firebase is configured for the deployed website.</p><h2>What not to send</h2><p>Please do not send account passwords, payment card details or other highly sensitive credentials through the enquiry or review forms.</p><h2>Contact</h2><p>For privacy-related questions, email <a href="mailto:buddycomputersofficial@gmail.com">buddycomputersofficial@gmail.com</a>.</p></section>'''

not_found = '''<section class="not-found"><div class="container"><span class="kicker">404 · PAGE NOT FOUND</span><h1>This page took<br><span>a wrong turn.</span></h1><p>The page you’re looking for doesn’t exist or has moved.</p><a class="btn primary" href="/">Back to home <span>↗</span></a></div></section>'''

pages = [
    ('index.html','home','Buddy Computers | Doorstep Computer Repair & IT Services in Ahmedabad','Doorstep PC and laptop repair, custom builds, office networking, websites and digital services across Ahmedabad. Home and office visits by appointment.',home,'/'),
    ('services/index.html','services','Computer Repair, Networking & Digital Services in Ahmedabad | Buddy Computers','Explore PC repair, Windows support, upgrades, custom PC builds, networking, IT support, websites, video editing and SEO services in Ahmedabad.',services_page,'/services/'),
    ('about/index.html','about','About Buddy Computers | Doorstep Technology Support in Ahmedabad','Learn how Buddy Computers provides appointment-based computer repair, IT support, networking and digital services across Ahmedabad.',about,'/about/'),
    ('contact/index.html','contact','Contact Buddy Computers | Call, WhatsApp or Book a Service in Ahmedabad','Contact Navin Sharma or Shubham Jangir for doorstep computer repair and IT services across Ahmedabad. Available Monday to Sunday, 10 AM to 8 PM.',contact,'/contact/'),
    ('reviews/index.html','reviews','Customer Reviews | Buddy Computers Ahmedabad','Read approved Buddy Computers customer reviews or submit your own review after using our computer, IT or digital services.',reviews,'/reviews/'),
    ('privacy/index.html','privacy','Privacy | Buddy Computers','Privacy information for Buddy Computers website enquiries, customer reviews and Firebase-backed website features.',privacy,'/privacy/'),
]

for rel,active,title,desc,body,path in pages:
    target=OUT/rel; target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(shell(active,title,desc,body,path),encoding='utf-8')

(OUT/'404.html').write_text(shell('', 'Page not found | Buddy Computers','The requested Buddy Computers page could not be found.',not_found,'/404',True),encoding='utf-8')

# Admin page is intentionally noindex and uses a standalone app shell.
admin_body = r'''<section class="admin-shell" data-admin-app><div class="admin-login" data-admin-login><div class="admin-login-card"><div class="admin-brand"><div class="admin-brand-lockup"><img src="/assets/buddy-symbol.png" alt="" width="512" height="512"><strong><b>Buddy</b> <i>Computers</i></strong></div><span>ADMIN PANEL</span></div><h1>Welcome back.</h1><p>Sign in with the Firebase Authentication admin account configured for Buddy Computers.</p><form class="form-stack" data-admin-login-form><label><span>Email</span><input type="email" name="email" required autocomplete="username" placeholder="buddycomputersofficial@gmail.com"></label><label><span>Password</span><input type="password" name="password" required autocomplete="current-password" placeholder="••••••••"></label><button class="btn primary full" type="submit">Sign in <span>↗</span></button><button class="text-button" type="button" data-reset-password>Forgot password?</button><p class="form-status" data-admin-login-status role="status"></p></form><div class="admin-setup-note" data-admin-setup-note hidden><strong>Firebase is not configured yet.</strong><span>Follow FIREBASE_SETUP.md in the project ZIP, then update <code>dist/assets/firebase-config.js</code>.</span></div></div></div><div class="admin-dashboard" data-admin-dashboard hidden><aside class="admin-sidebar"><div class="admin-side-brand"><img src="/assets/buddy-symbol.png" alt="" width="512" height="512"><span>Buddy Admin</span></div><nav><button class="active" data-admin-tab="overview">Overview</button><button data-admin-tab="enquiries">Enquiries <b data-enquiry-badge>0</b></button><button data-admin-tab="reviews">Reviews <b data-review-badge>0</b></button></nav><div class="admin-side-bottom"><span data-admin-email></span><button type="button" data-admin-logout>Sign out</button><a href="/" target="_blank">Open website ↗</a></div></aside><main class="admin-main"><header class="admin-topbar"><div><span class="kicker">BUDDY COMPUTERS</span><h2 data-admin-title>Overview</h2></div><button class="admin-mobile-menu" type="button" data-admin-nav-toggle>☰</button></header><section class="admin-view" data-view="overview"><div class="admin-stats"><article><span>New enquiries</span><strong data-stat-new-enquiries>0</strong><small>Waiting for action</small></article><article><span>Pending reviews</span><strong data-stat-pending-reviews>0</strong><small>Waiting for approval</small></article><article><span>Approved reviews</span><strong data-stat-approved-reviews>0</strong><small>Visible on website</small></article><article><span>Total enquiries</span><strong data-stat-total-enquiries>0</strong><small>All records</small></article></div><div class="admin-panel"><div class="panel-head"><div><h2>Recent activity</h2><p>Latest enquiries and reviews.</p></div><button class="text-button" type="button" data-refresh>Refresh</button></div><div class="activity-list" data-activity-list></div></div></section><section class="admin-view" data-view="enquiries" hidden><div class="admin-panel"><div class="panel-head wrap"><div><h2>Enquiries</h2><p>Track every website enquiry from new to resolved.</p></div><div class="panel-tools"><input type="search" placeholder="Search enquiries" data-enquiry-search><select data-enquiry-filter><option value="all">All statuses</option><option value="new">New</option><option value="contacted">Contacted</option><option value="resolved">Resolved</option></select></div></div><div class="admin-table-wrap"><table class="admin-table"><thead><tr><th>Customer</th><th>Service / message</th><th>Received</th><th>Status</th><th>Actions</th></tr></thead><tbody data-enquiry-table></tbody></table></div><div class="mobile-records" data-enquiry-cards></div></div></section><section class="admin-view" data-view="reviews" hidden><div class="admin-panel"><div class="panel-head wrap"><div><h2>Reviews</h2><p>Approve only genuine customer feedback.</p></div><div class="panel-tools"><input type="search" placeholder="Search reviews" data-review-search><select data-review-filter><option value="all">All statuses</option><option value="pending">Pending</option><option value="approved">Approved</option><option value="rejected">Rejected</option></select></div></div><div class="admin-table-wrap"><table class="admin-table"><thead><tr><th>Customer</th><th>Review</th><th>Received</th><th>Status</th><th>Actions</th></tr></thead><tbody data-review-table></tbody></table></div><div class="mobile-records" data-review-cards></div></div></section></main></div><div class="toast" data-toast role="status" aria-live="polite"></div></section>'''
admin_html = f'''<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="Private Buddy Computers administration panel for enquiries and customer review moderation."><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#f7fbff"><title>Buddy Computers Admin</title><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png"><script src="/assets/theme.js"></script><script src="/assets/firebase-config.js"></script><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/admin.css"></head><body>{admin_body}<script type="module" src="/assets/admin.js"></script></body></html>'''
admin_target=OUT/'admin/index.html'; admin_target.parent.mkdir(parents=True,exist_ok=True); admin_target.write_text(admin_html,encoding='utf-8')

# SEO files
sitemap_urls=[SITE_URL+'/',SITE_URL+'/services/',SITE_URL+'/about/',SITE_URL+'/contact/',SITE_URL+'/reviews/',SITE_URL+'/privacy/']
sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in sitemap_urls)+'</urlset>\n'
(OUT/'sitemap.xml').write_text(sitemap,encoding='utf-8')
(OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /admin/\nSitemap: {SITE_URL}/sitemap.xml\n',encoding='utf-8')
print(f'Generated {len(pages)} public pages, admin panel, 404 and SEO files.')
