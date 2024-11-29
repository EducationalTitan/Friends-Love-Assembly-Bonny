from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)  # Use 'last_name' instead of 'second_name'
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Ensure email is unique
    date_of_birth = models.DateField()
    home_address = models.TextField()
    state_of_origin = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Field for image uploads
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title