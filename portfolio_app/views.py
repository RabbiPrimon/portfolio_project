from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Profile, Skill, Experience, Education, Project, Service, Tool, BlogPost, ContactMessage
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    skills = list(Skill.objects.all())
    experiences = Experience.objects.all()
    services = Service.objects.filter(is_active=True)
    tools = Tool.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()

    # Merge services and tools into skills for unified display
    for service in services:
        skills.append(type('Skill', (), {
            'name': service.title,
            'icon': service.icon,
            'category': 'service',
            'proficiency': 100,  # Assume full proficiency for services
            'id': f'service_{service.id}'
        })())

    for tool in tools:
        skills.append(type('Skill', (), {
            'name': tool.name,
            'icon': tool.icon,
            'category': 'tool',
            'proficiency': 100,  # Assume full proficiency for tools
            'id': f'tool_{tool.id}'
        })())

    return render(request, 'home.html', {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'projects': projects,
    })

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    return render(request, 'about.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    return render(request, 'project_detail.html', {
        'project': project,
        'images': images,
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {
        'services': services,
    })

def portfolio(request):
    portfolio_items = Project.objects.all()
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

def experience_timeline(request):
    experiences = Experience.objects.all()
    return render(request, 'experience.html', {
        'experiences': experiences,
    })

def tools(request):
    tools = Tool.objects.all()
    return render(request, 'tools.html', {
        'tools': tools,
    })



def blog(request):
    blog_posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(blog_posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {
        'page_obj': page_obj,
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog_detail.html', {
        'post': post,
    })
