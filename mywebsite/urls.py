from django.contrib import admin
from django.urls import path, include
from portfolio import views  # استيراد views الخاصة بالتطبيق
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('Home/', views.Home, name='Home'),
    path('About/', views.About, name='About'),
    path('Projects/', views.Projects, name='Projects'),
    path('Blog/', views.Blog, name='Blog'),
path('Contact/', views.Contact, name='Contact'),
path('blogs/', views.blog_create, name='blog_read'),
    path('create/', views.blog_create, name='blog_create'),
path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/<int:pk>/edit/', views.blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
path('blogs/new/', views.blog_create, name='blog_create'),
path('blogs/', views.blog_list, name='blog_list'),
path('contact/', views.contact_view, name='contact'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
