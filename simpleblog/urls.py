from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # path('ckeditor', include('ckeditor_uplaoders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
