from .models import Category, Site, Post, Profile
from django.db.models import Count
from taggit.models import Tag

def extras(request):
    site = Site.objects.all().first()
    profile = Profile.objects.all().first()
    cats = Category.objects.all()
    recent_post = Post.objects.all()[:5]
    tags = Tag.objects.all()
    cat_dict = {} 
    for cat in cats:
        cat_dict[cat.pk] = Post.objects.filter(category=cat).count()

    tags2 = tags.annotate(num_times=Count('taggit_taggeditem_items'))
    tag_count_dict = {}
    for tag in tags2:
        tag_count_dict[tag.name] = tag.num_times

    site_key_words = list()
    if site is not None:
        site_key_words = ",".join(list(site.key_words.names()))

    return {'cats':cats,'recent_post':recent_post,'tags':tags,'tag_count_dict':tag_count_dict,'profile':profile,'cat_dict':cat_dict,'site':site,'site_key_words':site_key_words}