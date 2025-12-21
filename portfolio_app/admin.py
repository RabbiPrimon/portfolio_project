from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Experience, Service, Project, ProjectImage, Tool, Testimonial, BlogPost, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'freelance_available', 'created_at')
    search_fields = ('name', 'role', 'email')
    list_filter = ('freelance_available', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'role', 'tagline', 'bio')}),
        ('Contact', {'fields': ('email', 'github', 'linkedin', 'youtube')}),
        ('Details', {'fields': ('profile_photo', 'years_of_experience', 'location', 'freelance_available')}),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'display_order', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
    list_editable = ('display_order', 'proficiency')
    ordering = ('display_order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'display_order')
    search_fields = ('job_title', 'company', 'technologies')
    list_filter = ('start_date', 'end_date')
    list_editable = ('display_order',)
    ordering = ('-start_date',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'display_order', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created_at')
    list_editable = ('display_order', 'is_active')
    ordering = ('display_order',)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    ordering = ('display_order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'display_order', 'created_at')
    search_fields = ('title', 'tech_stack', 'category')
    list_filter = ('category', 'featured', 'created_at')
    list_editable = ('featured', 'display_order')
    ordering = ('-featured', 'display_order')
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'description', 'category', 'tech_stack')}),
        ('Media', {'fields': ('thumbnail', 'video_url')}),
        ('Links', {'fields': ('github_link', 'demo_link')}),
        ('Settings', {'fields': ('featured', 'display_order')}),
    )
    inlines = [ProjectImageInline]

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'display_order')
    search_fields = ('project__title', 'caption')
    list_filter = ('project',)
    ordering = ('project', 'display_order')

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon', 'display_order', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
    list_editable = ('display_order',)
    ordering = ('display_order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'role_company', 'display_order', 'is_active', 'created_at')
    search_fields = ('client_name', 'role_company', 'feedback')
    list_filter = ('is_active', 'created_at')
    list_editable = ('display_order', 'is_active')
    ordering = ('display_order',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'publish_date')
    search_fields = ('title', 'content', 'tags')
    list_filter = ('is_published', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish_date',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
