from django.db import models
from blog.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class PostTypeModel(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True,upload_to="images/")
    body = models.TextField()
    video = models.TextField(default="")
    pub_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
      abstract = True