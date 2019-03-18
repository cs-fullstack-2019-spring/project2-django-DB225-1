from django.conf import settings
from django.urls import path, include
from django.views.static import serve

from . import views

urlpatterns = [
    # the home page
    path('', views.index, name="index"),
    # the root for all entries
    path('allEntries/', views.allEntries, name="allEntries"),
    # create a new user account
    path('newAccount/', views.newAccount, name="newAccount"),

    # add a new entry
    path('newEntry/', views.newEntry, name="newEntry"),
    # all the entry I made
    path('yourEntries/', views.yourEntries, name="yourEntries"),
    # the root for the page with all the details about the entry
    path('readEntry/<int:entry_id>/', views.readEntry, name="readEntry"),
    # edit this entry
    path('editEntry/<int:entry_id>/', views.editEntry, name="editEntry"),
    # delete this entry
    path('deleteEntry/<int:delete_id>/', views.deleteEntry, name="deleteEntry"),

    # add some bonus informations about an entry
    path('newRelatedItems/<int:item_id>/', views.newRelatedItems, name="newRelatedItems"),
    # edit this bonus info
    path('editRelatedItems/<int:item_id>/', views.editRelatedItems, name="editRelatedItems"),
    # delete the bonus info
    path('deleteRelatedItems/<int:delete_item>/', views.deleteRelatedItems, name="deleteRelatedItems"),

    # the page of the result of search via the search bar
    path('searchPosts/', views.search, name="search"),
    # the path for the images
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
