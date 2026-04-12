# 🏋️ Realtime Gym — Full Django Website
### Salem, Tamil Nadu | Python Fullstack | Modern Dark UI

## 🚀 Quick Start

```bash
cd realtimegym
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Website: http://127.0.0.1:8000/
Admin:   http://127.0.0.1:8000/admin/

## ✨ All Sections
Hero | Ticker | About | Services (6) | Trainers (4) | Schedule (Mon-Sun) | Pricing (3 plans) | BMI Calculator | Testimonials Slider | Gallery | Instagram Strip | Blog | Contact + Map | Footer

## 📁 Structure
gym/templates/gym/
  base.html        — Nav, Footer, WhatsApp button
  index.html       — Full homepage
  blog.html        — Blog listing
  blog_detail.html — Blog post page

gym/models.py  — ContactMessage, MembershipEnquiry, Testimonial, BlogPost
gym/admin.py   — Full admin for all models

## ✏️ Customize
Search index.html for: +91 98765 43210, @RealtimeGym, info@realtimegym.in
Pricing: search 999, 1799, 2999

## 🌐 Deploy (Render.com)
Build: pip install -r requirements.txt
Start: python manage.py migrate && gunicorn realtimegym.wsgi
Production: Set DEBUG=False, ALLOWED_HOSTS=['yourdomain.com']

Built with ❤️ for Realtime Gym, Salem.
