from django.urls import path
from .views import UserRegisterView, PasswordsChangeView,EditProfilePageView,CreateProfilePageView, UserEditView, ShowProfilePageView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	#path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"), name='edit_profile'),
	path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html"), name='password_change'),
	path('password_sucess/', views.password_sucess, name="password_sucess"),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
	path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile_page"),
]
