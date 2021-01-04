from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from taggit.managers import TaggableManager
import os

# Create your models here.


# Retrieve name and extension of filepath
def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, extension = os.path.splitext(base_name)
    return name, extension


def upload_image_path(instance, filename):
    name, extension = get_filename_extension(filename)
    final_name = f"{instance.id}-{instance.title}{extension}"
    return f"posts/{final_name}"


class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(status='published')


class Post(models.Model):
    objects = PostManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    tags = TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
