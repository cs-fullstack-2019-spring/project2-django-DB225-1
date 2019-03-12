from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('allEntries/', views.allEntries, name="allEntries"),
    path('newAccount/', views.newAccount, name="newAccount"),

    path('newEntry/', views.newEntry, name="newEntry"),
    path('yourEntries/<int:entry_id>/', views.yourEntries, name="yourEntries"),
    path('readEntry/<int:entry_id>/', views.readEntry, name="readEntry"),
    path('editEntry/<int:entry_id>/', views.editEntry, name="editEntry"),
    path('deleteEntry/<int:delete_id>/', views.deleteEntry, name="deleteEntry"),

    path('newRelatedItems/<int:item_id>/', views.newRelatedItems, name="newRelatedItems"),
    path('readRelatedItems/<int:item_id>/', views.readRelatedItems, name="readRelatedItems"),
    path('editRelatedItems/<int:item_id>/', views.editRelatedItems, name="editRelatedItems"),
    path('deleteRelatedItems/<int:delete_item>/', views.deleteRelatedItems, name="deleteRelatedItems"),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
