from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
        'bio': forms.TextInput(attrs={'class': 'form-control'}),
        # 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
        'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = ('bio', 'profile_pic', 'website_url','facebook_url','instagram_url','twitter_url','pinterest_url')
    

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self,*args,**kwargs):
        super(EditProfileForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

