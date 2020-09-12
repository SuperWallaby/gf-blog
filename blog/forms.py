from django import forms
from .models import Post,  Comment

class CommentForm(forms.ModelForm):
		class Meta:
			model = Comment
			fields = ('name', 'body')

			widgets = {
				'name': forms.TextInput(),
				'body': forms.Textarea(attrs={'id':"comment", 'name':"body", 'cols':"45", 'rows':"8", 'required':"required"}),
			}