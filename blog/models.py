from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from share import models as share_models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_editorjs import EditorJsField


class SubScriber(models.Model):
    mail = models.EmailField(default="")


class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")
    date_added = models.DateTimeField(auto_now_add=True)


class Gallery(models.Model):
    thumb = models.ImageField(
        null=True, blank=True, upload_to="images/", help_text="1024X680", default="")
    photo_small = models.ImageField(
        null=True, blank=True, upload_to="images/", help_text="900X600", default="")
    photo_large = models.ImageField(
        null=True, blank=True, upload_to="images/", help_text="1400X1000", default="")
    description = models.CharField(
        max_length=50, null=True, blank=True, default="")

    def get_small(self):
        if bool(self.photo_small):
            return self.photo_small
        elif bool(self.photo_large):
            return self.photo_large
        elif bool(self.thumb):
            return self.thumb

    def get_large(self):
        if bool(self.photo_large):
            return self.photo_large
        elif bool(self.photo_small):
            return self.photo_small
        elif bool(self.thumb):
            return self.thumb

    def get_thumb(self):
        if bool(self.thumb):
            return self.thumb
        elif bool(self.photo_large):
            return self.photo_large
        elif bool(self.photo_small):
            return self.photo_small


class Profile(models.Model):
    name = models.CharField(max_length=50, default="")
    phone_num = models.CharField(
        max_length=50, null=True, blank=True, default="")
    job = models.CharField(max_length=50, default="")
    photo_small = models.ImageField(
        null=True, blank=True, upload_to="images/", help_text="300X300")
    photo_big = models.ImageField(
        null=True, blank=True, upload_to="images/", help_text="600X600")
    description = models.TextField(help_text="long Description")
    description_short = models.TextField(help_text="Short Description")

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)


class Site(models.Model):
    title = models.CharField(max_length=100, default='')
    key_words = TaggableManager(blank=True)
    description_short = models.TextField(help_text="Short Description")
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    email = models.EmailField(max_length=100)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    twitter = models.CharField(blank=True, null=True, max_length=100)
    insta = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255, help_text="short text describe this category", default="", null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s' % (self.name)


def pre_save_category_signal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug2(instance)


def create_slug2(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug2(instance, new_slug=new_slug)
    return slug


pre_save.connect(pre_save_category_signal_receiver, sender=Category)


class Post(share_models.PostTypeModel):
    category = models.ForeignKey(
        Category, null=True, default=None, blank=True, on_delete=models.SET_NULL)
    pop_in_banner = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    read_time = models.IntegerField(help_text="Time to read (Unit:minutes)")
    tags = TaggableManager(blank=True)
    view_count = models.IntegerField(default=0)
    photo = models.ForeignKey(Gallery, default=None,
                              blank=True, null=True, on_delete=models.SET_NULL)
    body = EditorJsField(editorjs_config={
        'holder': 'holder',
        "tools": {
            "Table": {
                "disabled": False,
                "inlineToolbar": True,
                "config": {"rows": 2, "cols": 3, },
            }
        }
    })

    def tag_names(self):
        return self.tags.names()

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article-detail', args=[self.slug])

    class Meta:
        ordering = ["-pub_date", "-timestamp"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_signal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_signal_receiver, sender=Post)


class Like(models.Model):
    ip = models.CharField(max_length=16)
    like = models.ForeignKey(Post, related_name="like",
                             on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    face = models.CharField(max_length=10, default="1", null=True, blank=True)
    password = models.CharField(max_length=20, default="")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def child(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False1
        return True
