# Django Portfolio Website

A fully dynamic, modern, dark-themed portfolio website built with Django MVT architecture. All content is admin-driven, making it easy to manage without touching code.

## Features

- **Dark Futuristic UI** with glassmorphism effects
- **100% Admin-Driven** content management
- **Responsive Design** for all devices
- **Dynamic Sections**: Hero, About, Skills, Experience Timeline, Services, Projects, Tools, Testimonials, Blog, Contact
- **Rich Text Editing** with CKEditor
- **Image Uploads** and media management
- **SEO-Friendly** URLs and structure
- **Contact Form** with admin message management

## Tech Stack

- **Backend**: Python, Django 5.0
- **Database**: SQLite (easily switchable to PostgreSQL)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Rich Text**: CKEditor
- **Media Handling**: Pillow

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the site**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel
- Login to `/admin/` with your superuser credentials
- Add content to all sections through the admin interface
- Upload images, write rich text content, manage ordering

### Content Management
- **Profile**: Basic info, bio, social links
- **Skills**: Name, category, proficiency, icon
- **Experience**: Job history with timeline
- **Services**: Offered services with icons
- **Projects**: Portfolio items with images and details
- **Tools**: Technologies and tools used
- **Testimonials**: Client feedback
- **Blog Posts**: Articles with rich content
- **Contact Messages**: View and manage inquiries

## Deployment

### Production Settings
- Set `DEBUG=False` in settings.py
- Configure `ALLOWED_HOSTS`
- Use a production database (PostgreSQL recommended)
- Set up static files serving (nginx/apache)
- Configure media files serving
- Use environment variables for secrets

### Example Production Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Project Structure

```
portfolio_project/
├── portfolio_app/
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── admin.py           # Admin configurations
│   ├── urls.py            # App URLs
│   ├── forms.py           # Contact form
│   └── migrations/        # Database migrations
├── portfolio_project/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URLs
│   └── wsgi.py            # WSGI config
├── Templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Customization

### Styling
- Edit `static/css/style.css` for custom styles
- Modify templates in `Templates/` directory
- Use Bootstrap classes for responsive design

### Adding New Sections
1. Create model in `models.py`
2. Register in `admin.py`
3. Add view in `views.py`
4. Create URL pattern in `urls.py`
5. Create template in `Templates/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue on GitHub or contact the maintainer.
