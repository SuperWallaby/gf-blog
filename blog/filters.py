import django_filters
from django import forms
from .models import *


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',label='',widget=forms.TextInput(attrs={'placeholder': 'Search Title', 'class': 'form-control form-control-lg'}))

    class Meta:
        model = Post
        fields = ['title']
