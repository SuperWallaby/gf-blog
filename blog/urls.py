from django.urls import path
from .views import HomeView, ArticleDetail, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView,CategoryListView,LikeView,AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]

