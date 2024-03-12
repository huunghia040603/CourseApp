from django.db import models
from  django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from  cloudinary.models import CloudinaryField


class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = CloudinaryField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return self.name