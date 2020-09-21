from django import forms
from .models import Post,  Comment
from django.utils.text import slugify
import unidecode
from unidecode import unidecode


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(),
            'body': forms.Textarea(attrs={'id': "comment", 'name': "body", 'cols': "45", 'rows': "8", 'required': "required"}),
        }


class PostForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        print(slugify(self.cleaned_data.get("title")))
        post.slug = slugify(
            unidecode(self.cleaned_data.get("title")), allow_unicode=True)
        post.save()
        return post

    class Meta:
        model = Post
        fields = ['title', 'intro', 'body', 'category',
                  'pop_in_banner', 'read_time', 'tags']
