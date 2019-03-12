from django.contrib import admin
from .models import UserLoginModel, PostModel, RelatedItemsModel

# Register your models here.
admin.site.register(UserLoginModel)
admin.site.register(PostModel)
admin.site.register(RelatedItemsModel)
