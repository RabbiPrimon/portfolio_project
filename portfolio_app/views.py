from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Profile, Skill, Project, Service, PortfolioItem, ContactMessage
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })
def new_page(request):

    return render(request, 'new.html')

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {
        'profile': profile,
        'skills': skills,
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {
        'project': project,
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {
        'services': services,
    })

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {
        'portfolio_items': portfolio_items,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form,
    })
