from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserVizit(AbstractUser):
    about = models.TextField()
    avatar = models.ImageField(storage="/images/avatars")
    job = models.CharField(max_length=64,null=True,blank=True)
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.username

class Stack(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class StackUserRelate(models.Model):
    user_id = models.ForeignKey(UserVizit,on_delete=models.CASCADE)
    stack_id = models.ForeignKey(Stack,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    author = models.ForeignKey(UserVizit, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    preview_image=models.ImageField(storage="/images/preview")
    def __str__(self):
        return self.title

class ImagesPost(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(storage="/images/images_post")

class Icon(models.Model):
    name=models.CharField(max_length=60)
    image = models.ImageField(storage="/images/icons")

class LinksAcc(models.Model):
    user_id = models.ForeignKey(UserVizit,on_delete=models.CASCADE)
    link = models.CharField(max_length=120)
    icon = models.ForeignKey(Icon,on_delete=models.SET_NULL, null=True, blank=True)