from django import forms
from .models import UserLoginModel, PostModel, RelatedItemsModel


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        exclude = ['userForeignKey']
        widgets = {
            "password": forms.PasswordInput()
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['postForeignKey']


class RelatedItemsForm(forms.ModelForm):
    class Meta:
        model = RelatedItemsModel
        exclude = ['itemForeignKey']
