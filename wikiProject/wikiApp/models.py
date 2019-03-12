from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserLoginModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    userForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class PostModel(models.Model):
    title_Post = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField()
    postForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title_Post


class RelatedItemsModel(models.Model):
    title_Item = models.CharField(max_length=200)
    some_text = models.TextField()
    logo = models.ImageField()
    itemForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title_Item
