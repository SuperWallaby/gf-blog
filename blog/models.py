from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    BOOKING = 'BK'
    TEMPLATE_A = 'TA'
    TIME_SAPCE = 'TS'
    SUPER_CLASS = (
    ('BK', 'BOOKING'),
    ('TS', 'TIME_SAPCE'),
    ('TA', 'TEMPLATE_A'),
    )

    label = models.CharField(max_length=255)
    name = models.SlugField(max_length=255)
    super_class = models.CharField(
        max_length=2,
        choices=SUPER_CLASS,
        default=BOOKING,
    )

    def __str__(self):
        return '%s - %s' % (self.super_class, self.label)

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    pinterest_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True,upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    video = models.TextField(default="")
    pub_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="blog_posts")
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
