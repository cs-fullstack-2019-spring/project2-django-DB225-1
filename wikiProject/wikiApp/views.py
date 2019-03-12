from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserLoginModel, UserLoginForm, RelatedItemsModel, PostModel, PostForm

# Create your views here.
def index(request):
    return render(request, 'wikiApp/index.html')


def newAccount(request):
    return render(request, 'wikiApp/newAccount.html')


def allEntries(request):
    return render(request, 'wikiApp/allEntries.html')


def newEntry(request):
    return render(request, 'wikiApp/newEntry.html')


def yourEntries(request, entry_id):
    return render(request, 'wikiApp/yourEntries.html')


def readEntry(request, entry_id):
    return render(request, 'wikiApp/readEntry.html')


def editEntry(request, entry_id):
    return render(request, 'wikiApp/editEntry.html')


def deleteEntry(request, delete_id):
    return render(request, 'wikiApp/deleteEntry.html')


def newRelatedItems(request, entry_id):
    return render(request, 'wikiApp/newRelatedEntry.html')


def readRelatedItems(request, item_id):
    return render(request, 'wikiApp/readRelatedEntry.html')


def editRelatedItems(request, item_id):
    return render(request, 'wikiApp/editRelatedEntry.html')


def deleteRelatedItems(request, delete_item):
    return render(request, 'wikiApp/deleteRelatedEntry.html')
