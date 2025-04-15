
from django.contrib import admin
from .models import Home, About, Projects, Blog, Contact
from modeltranslation.admin import TranslationAdmin


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title', 'description')

@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    pass


