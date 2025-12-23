# TODO List for Django Portfolio Website Expansion

## Models and Database
- [x] Expand models.py: Add categories, icons, display_order to Skill
- [x] Add new models: Experience, Tool, Testimonial, BlogPost, ProjectImage
- [x] Run migrations for new models

## Admin
- [x] Update admin.py: Register new models, add rich text editors, image previews, filters
- [x] Add ProjectImageInline to ProjectAdmin

## Views
- [x] Update views.py: Add views for timeline, tools, testimonials, blog, project detail with multiple images
- [x] Add missing views: experience_timeline, tools, testimonials, blog, blog_detail

## URLs
- [x] Update portfolio_app/urls.py: Add paths for new sections

## Templates
- [x] Update Templates/base.html: Switch to dark theme
- [x] Update Templates/home.html: Add new sections (Hero with CTA, About with details, Skills with categories, etc.)
- [x] Update other templates: about.html, projects.html, services.html, contact.html
- [x] Create new templates: timeline.html (experience.html), tools.html, testimonials.html, blog.html, blog_detail.html

## Static Files
- [x] Enhance static/css/style.css: Dark theme, glassmorphism, animations

## Settings
- [x] Update portfolio_project/settings.py: Ensure media handling, security
- [x] Add ckeditor to INSTALLED_APPS

## Configuration Files
- [x] Create requirements.txt
- [x] Create .env.example
- [x] Create README.md with setup instructions

## Testing and Deployment Prep
- [x] Test all new views and templates
- [x] Ensure responsive design and dark theme
- [x] Run collectstatic for deployment

## Current Progress
- [x] Update about.html to dark theme
- [x] Update projects.html to dark theme
- [x] Update services.html to dark theme
- [x] Update contact.html to dark theme
- [x] Enhance CSS with more glassmorphism and animations
- [x] Test site functionality
