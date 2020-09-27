from django.db import models
from blog.models import User
# Create your models here.


class PostTypeModel(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField(max_length=255, default="")
    pub_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
