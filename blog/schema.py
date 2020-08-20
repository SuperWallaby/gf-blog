from graphene_django import DjangoObjectType
from .models import Post, Category, Comment
import graphene
from graphene import ObjectType, Schema


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class Query(ObjectType):
    # Previous fields here ...
    all_Posts = graphene.List(PostType)
    all_Category = graphene.List(CategoryType)
    all_Comment = graphene.List(CommentType)

    def resolve_all_Category(self, info, **kwargs):
        return Category.objects.all() 

    def resolve_all_Posts(self, info, **kwargs):
        return Post.objects.all() 

    def resolve_all_Comment(self, info, **kwargs):
        return Comment.objects.all() 

    def resolve_car(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Car.objects.get(id=id)

schema = Schema(query=Query)