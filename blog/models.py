from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from share import models as share_models

class Category(models.Model):
    label = models.CharField(max_length=255)
    name = models.SlugField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.super_class, self.label)

    def get_absolute_url(self):
        return reverse('home')

class Post(share_models.PostTypeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_posts",blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
