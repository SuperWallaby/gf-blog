from django import forms
from .models import Post, Category, Comment

names = Category.objects.all().values('name')
super_classes = Category.objects.all().values('super_class')

def myfn(a,b):
    return (a['name'], a['name'] + " | " + b['super_class'])

choices = map(myfn, names, super_classes)

choice_list = []

for item in choices:
	print(choices);
	choice_list.append(item)

print(choice_list)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'body', 'header_image')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control'}),
		'author': forms.Select(attrs={'class': 'form-control'}),
		'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
		}

class EditForm(forms.ModelForm):
		class Meta:
			model = Post
			fields = ('title', 'author', 'category', 'body')
			widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control', 'id':"elder"}),
			'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
			}

class CommentForm(forms.ModelForm):
		class Meta:
			model = Comment
			fields = ('name', 'body')

			widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'id':"elder"}),
			}

	