from django.urls import path
from .views import HomeView, ArticleDetail, CategoryView,CategoryListView,LikeView,AddCommentView, AboutView, BlogView, GalleryListView, SearchView, TagsView, TagsListView, ThanksView, SubScribeView,AddContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
    path('category/<slug:slug>/', CategoryView, name='category'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('galleries/', GalleryListView.as_view(), name='galleries'),
    path('about/', AboutView, name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('tag_list/', TagsListView.as_view(), name='tag-list'),
    path('tags/<str:tags>', TagsView.as_view(), name='tags'),
    path('search/', SearchView.as_view(), name='search'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AboutView, name='add_comment'),
    path('liked_post/<slug:slug>', LikeView, name='liked_post'),
    path('added_post/<slug:slug>', AddCommentView, name='added_post'),
    path('subscribe/', SubScribeView, name='subscribe'),
    path('thanks/', ThanksView, name='thanks'),
    path('contact/', AddContactView, name='contact')
]

