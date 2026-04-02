📁 IMAGES FOLDER — How to use
================================

/images/
├── profile/
│   └── avatar.jpg          ← Your profile photo (used in About section & hero)
│                              Recommended size: 400x400px, square
│
├── projects/
│   ├── project-1.jpg       ← Screenshot for "Enterprise Analytics Platform"
│   ├── project-2.jpg       ← Screenshot for "Automated Deployment Pipeline"
│   └── project-3.jpg       ← Screenshot for "FinTech Payment Gateway"
│                              Recommended size: 800x450px (16:9 ratio)
│
└── blog/
    ├── laravel-redis.jpg   ← Cover image for Laravel Queues blog post
    ├── docker-setup.jpg    ← Cover image for Docker Setup blog post
    └── freelancing.jpg     ← Cover image for Freelancing blog post
                               Recommended size: 1200x630px (og:image size)

HOW TO USE IN HTML:
-------------------
From index.html:
  <img src="images/profile/avatar.jpg" alt="Arafatul">
  <img src="images/projects/project-1.jpg" alt="Analytics Platform">

From blog/any-post.html:
  <img src="../images/blog/laravel-redis.jpg" alt="Cover">

TIPS:
-----
- Keep images under 500KB each
- Use .jpg for photos, .png for screenshots with text
- Compress at: https://squoosh.app (free, in browser)
- Best format: .webp (smallest size, best quality)
