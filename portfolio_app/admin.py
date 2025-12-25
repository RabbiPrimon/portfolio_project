from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Skill, Experience, Education, Project, ProjectImage, Service, Tool, BlogPost, ContactMessage
from ckeditor.widgets import CKEditorWidget
from django import forms

class EducationAdminForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y')
    )
    end_date = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y')
    )

    class Meta:
        model = Education
        fields = '__all__'

class EducationAdmin(admin.ModelAdmin):
    form = EducationAdminForm

class ProfileAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class ExperienceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y')
    )
    end_date = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y')
    )

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

admin.site.register(Education, EducationAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
