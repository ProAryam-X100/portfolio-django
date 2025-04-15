from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()



