from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from taggit.managers import TaggableManager
import os
import math
from django.db.models import Q
from tinymce import models as tinymce_models

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

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(tags__name__in=[query])
        )
        return self.published().filter(lookup).distinct()


class Post(models.Model):
    objects = PostManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    # body = models.TextField()
    body = tinymce_models.HTMLField()
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

    def when_published(self):
        now = timezone.now()

        diff = now - self.created

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            return str(seconds) + "ثانیه"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            return str(minutes) + " دقیقه"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            return str(hours) + " ساعت"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            return str(days) + " روز"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            return str(months) + " ماه"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            return str(years) + " سال"
