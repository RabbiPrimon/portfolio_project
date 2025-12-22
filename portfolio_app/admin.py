from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Skill, Experience, Project, ProjectImage, Service, Tool, Testimonial, BlogPost, ContactMessage
from ckeditor.widgets import CKEditorWidget
from django import forms

class ProfileAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class ExperienceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Experience
        fields = '__all__'

class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

class ServiceAdmin(admin.ModelAdmin):
    pass

class ToolAdmin(admin.ModelAdmin):
    pass

class TestimonialAdminForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Testimonial
        fields = '__all__'

class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    prepopulated_fields = {'slug': ('title',)}

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
