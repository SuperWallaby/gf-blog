from django.contrib import admin
from .models import Post, Category, Comment, Site, Like, Profile, Gallery, Skill, SubScriber,Contact
from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

# @admin.register(Site)
# class SiteAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#     pass

admin.site.register(Contact)
admin.site.register(SubScriber)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Site)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Gallery)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)