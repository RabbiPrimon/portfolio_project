# TODO List for Django Portfolio Website Expansion

## Models and Database
- [x] Expand models.py: Add categories, icons, display_order to Skill
- [x] Add new models: Experience, Tool, Testimonial, BlogPost, ProjectImage
- [x] Run migrations for new models

## Admin
- [ ] Update admin.py: Register new models, add rich text editors, image previews, filters
- [ ] Add ProjectImageInline to ProjectAdmin

## Views
- [ ] Update views.py: Add views for timeline, tools, testimonials, blog, project detail with multiple images
- [ ] Add missing views: experience_timeline, tools, testimonials, blog, blog_detail

## URLs
- [x] Update portfolio_app/urls.py: Add paths for new sections

## Templates
- [ ] Update Templates/base.html: Switch to dark theme
- [ ] Update Templates/home.html: Add new sections (Hero with CTA, About with details, Skills with categories, etc.)
- [ ] Update other templates: about.html, projects.html, services.html, contact.html
- [ ] Create new templates: timeline.html, tools.html, testimonials.html, blog.html, etc.

## Static Files
- [ ] Enhance static/css/style.css: Dark theme, glassmorphism, animations

## Settings
- [ ] Update portfolio_project/settings.py: Ensure media handling, security
- [ ] Add ckeditor to INSTALLED_APPS

## Configuration Files
- [ ] Create requirements.txt
- [ ] Create .env.example
- [ ] Create README.md with setup instructions

## Testing and Deployment Prep
- [ ] Test all new views and templates
- [ ] Ensure responsive design and dark theme
- [ ] Run collectstatic for deployment
