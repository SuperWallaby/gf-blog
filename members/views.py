from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blog.models import Profile


class CreateProfilePageView(generic.CreateView):
		model = Profile
		form_class = ProfilePageForm
		# fields = "__all__"
		template_name = "registration/create_user_profile_page.html"

		def form_valid(self, form):
			form.instance.user = self.request.user
			return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
		model = Profile
		form_class = ProfilePageForm
		template_name = "registration/edit_profile_page.html"
		success_url = reverse_lazy('home')
		# fields = ['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pinterest_url']


class ShowProfilePageView(generic.DetailView):
		model = Profile
		template_name = 'registration/user_profile.html'

		def get_context_data(self, *args, **kwargs):
			context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
			page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
			print('page_user.bio')
			print(page_user.bio)
			context["page_user"] = page_user
			return context


class PasswordsChangeView(PasswordChangeView):
		form_class = PasswordChangingForm
		success_url = reverse_lazy('password_sucess')

def password_sucess(request):
    	return render(request, 'registration/password_sucess.html',{})

class UserRegisterView(generic.CreateView):
		form_class = SignUpForm
		template_name = 'registration/register.html'
		success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
		form_class = EditProfileForm
		template_name = 'registration/edit_profile.html'
		success_url = reverse_lazy('home')

		def get_object(self):
				return self.request.user
