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
    post_Title = models.CharField(max_length=200)
    post_Text = models.TextField()
    createdDateTime = models.DateTimeField(auto_now_add=True)
    updatedDateTime = models.DateTimeField(auto_now=True)
    post_Image = models.ImageField(upload_to="media/images/", null=True, blank=True)
    postForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.post_Title


class RelatedItemsModel(models.Model):
    item_Title = models.CharField(max_length=200)
    item_Text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)
    item_Image = models.ImageField(upload_to="images")
    itemForeignKey = models.ForeignKey(PostModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.item_Title
