from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('Home/', lambda request: render(request, 'Home.html'), name='Home'),
    path('About/', lambda request: render(request, 'About.html'), name='About'),
    path('Projects/', lambda request: render(request, 'Projects.html'), name='Projects'),
    path('Blog/', lambda request: render(request, 'Blog.html'), name='Blog'),
path('Contact/', lambda request: render(request, 'Contact.html'), name='Contact'),
path('', views.Home, name='Home'),
    path('create/', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/edit/', views.blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('', views.blog_home, name='blog_home'),
path('contact/', views.contact_view, name='contact'),



]
