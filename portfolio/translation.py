from modeltranslation.translator import TranslationOptions, translator
from .models import About, Home, Projects, Blog, Contact

class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class HomeTranslationOptions(TranslationOptions):
    fields = ('title','content')


class ProjectsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'phone', 'email')

translator.register(About, AboutTranslationOptions)
translator.register(Home, HomeTranslationOptions)
translator.register(Projects, ProjectsTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
