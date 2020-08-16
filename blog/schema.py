from graphene_django import DjangoObjectType
from .models import Post, Category
import graphene
from graphene import ObjectType, Schema

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

    # Previous resolver function
    def resolve_all_Category(self, info, **kwargs):
        return Category.objects.all() 

    # Previous resolver function
    def resolve_all_Posts(self, info, **kwargs):
        return Post.objects.all() 

    def resolve_car(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Car.objects.get(id=id)

schema = Schema(query=Query)