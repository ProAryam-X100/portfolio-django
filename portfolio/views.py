from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


def Home(request):
    blogs = Blog.objects.all()
    return render(request, 'portfolio/Home.html', {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = BlogForm()
    return render(request, 'portfolio/blog_form.html', {'form': form})

def About(request):
    return render(request, 'portfolio/About.html')

def Projects(request):
    return render(request, 'portfolio/Projects.html')

def Contact(request):
    return render(request, 'portfolio/Contact.html')

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'portfolio/blog_create.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request, 'portfolio/blog_delete.html', {'blog': blog})


def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'portfolio/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'blog': blog})


from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email='aryam91139@gmail.com',
            recipient_list=['aryam91139@gmail.com'],
            fail_silently=False,
        )
        success = True

    return render(request, 'portfolio/Home.html', {'success': success})
