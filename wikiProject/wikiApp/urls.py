from django.conf import settings
from django.urls import path, include
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('allEntries/', views.allEntries, name="allEntries"),
    path('newAccount/', views.newAccount, name="newAccount"),

    path('newEntry/', views.newEntry, name="newEntry"),
    path('yourEntries/', views.yourEntries, name="yourEntries"),
    path('readEntry/<int:entry_id>/', views.readEntry, name="readEntry"),
    path('editEntry/<int:entry_id>/', views.editEntry, name="editEntry"),
    path('deleteEntry/<int:delete_id>/', views.deleteEntry, name="deleteEntry"),

    path('newRelatedItems/<int:item_id>/', views.newRelatedItems, name="newRelatedItems"),
    path('editRelatedItems/<int:item_id>/', views.editRelatedItems, name="editRelatedItems"),
    path('deleteRelatedItems/<int:delete_item>/', views.deleteRelatedItems, name="deleteRelatedItems"),

    path('searchPosts/', views.search, name="search"),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
