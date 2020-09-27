from django import forms
from .models import Post, Comment, Gallery
from django.utils.text import slugify
import unidecode
from unidecode import unidecode
import time


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(),
            'body': forms.Textarea(attrs={'id': "comment", 'name': "body", 'cols': "45", 'rows': "8", 'required': "required"}),
        }


class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        strtime = "".join(str(time.time()).split("."))
        slug = unidecode(post.title)
        string = "%s-%s" % (slug, strtime[7:])
        self.slug = slugify(string, allow_unicode=True)

        post.save()
        return post

    class Meta:
        model = Post
        fields = ['title', 'intro', 'body', 'category',
                  'pop_in_banner', 'read_time', 'tags']
