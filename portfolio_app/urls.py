from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('experience/', experience_timeline, name='experience'),
    path('projects/', projects, name='projects'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('services/', services, name='services'),
    path('tools/', tools, name='tools'),

    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]
