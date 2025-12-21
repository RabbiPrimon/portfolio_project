from django.urls import path
from portfolio_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/',projects, name='projects'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/',contact, name='contact'),
]
