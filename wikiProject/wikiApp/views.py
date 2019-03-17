from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserLoginModel, UserLoginForm, RelatedItemsModel, RelatedItemsForm, PostModel, PostForm
from django.db.models import Q


# Create your views here.

# The welcome page
def index(request):
    allPosts = PostModel.objects.all()
    return render(request, 'wikiApp/index.html', {'allPosts': allPosts})


# Create a new Account
def newAccount(request):
    newprofile = UserLoginForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and newprofile.is_valid():
        UserLoginModel.objects.create(username=request.POST["username"], email=request.POST['email'],
                                      password=request.POST["password"])
        User.objects.create_user(request.POST["username"], request.POST['email'], request.POST["password"])
        return redirect("index")
    return render(request, 'wikiApp/newAccount.html', {"newprofile": newprofile})


# Read the entries of all users
def allEntries(request):
    allPosts = PostModel.objects.all()
    return render(request, 'wikiApp/allEntries.html', {'allPosts': allPosts})


# Create a new entry
def newEntry(request):
    new_entry = PostForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and new_entry.is_valid():
        new_entry = PostForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        PostModel.objects.create(post_Title=request.POST["post_Title"], post_Text=request.POST["post_Text"],
                                 post_Image=request.FILES["post_Image"], postForeignKey=loggedInUser)

        return redirect('allEntries')
    else:
        print(new_entry.errors)
        print(new_entry.non_field_errors)
        new_entry = PostForm()
    return render(request, 'wikiApp/newEntry.html', {'new_entry': new_entry})


# Personal entries of each user
def yourEntries(request):
    if request.user.is_authenticated:
        userLoggedIn = UserLoginModel.objects.get(username=request.user)
        personalInfo = PostModel.objects.filter(postForeignKey=userLoggedIn)
        return render(request, 'wikiApp/yourEntries.html', {"personalInfo": personalInfo})
    else:
        return render(request, 'wikiApp/yourEntries.html')


# Click on the picture of any entry to have more informations
def readEntry(request, entry_id):
    relatedItem = RelatedItemsModel.objects.all()
    clickOnEntry = get_object_or_404(PostModel, pk=entry_id)
    print(relatedItem)
    return render(request, 'wikiApp/readEntry.html', {'clickOnEntry': clickOnEntry, 'relatedItem': relatedItem})


# Edit an entry
def editEntry(request, entry_id):
    edit_entry = get_object_or_404(PostModel, pk=entry_id)
    editedEntry = PostForm(request.POST or None, instance=edit_entry)
    if editedEntry.is_valid():
        editedEntry.save()
        return redirect('allEntries')
    return render(request, 'wikiApp/editEntry.html', {'editedEntry': editedEntry})


# Delete an entry
def deleteEntry(request, delete_id):
    delete_entry = get_object_or_404(PostModel, pk=delete_id)
    if request.method == 'POST':
        delete_entry.delete()
        return redirect('allEntries')
    return render(request, 'wikiApp/deleteEntry.html', {"delete_entry": delete_entry})


# Create an item related to an entry
def newRelatedItems(request, item_id):
    newItem = RelatedItemsForm(request.POST or None, request.FILES)
    if request.method == 'POST' and newItem.is_valid():
        print('doing this', request.method)
        ItemForEntries = get_object_or_404(PostModel, pk=item_id)
        item_image = ''
        if request.FILES:
            item_image = request.FILES['item_Image']

        RelatedItemsModel.objects.create(item_Title=request.POST['item_Title'], item_Text=request.POST['item_Text'],
                                         item_Image=item_image, itemForeignKey=ItemForEntries)
        return redirect('readEntry', entry_id=item_id)
    return render(request, 'wikiApp/newRelatedItems.html', {'form': newItem, "item_id": item_id})


# Edit the item related to an entry
def editRelatedItems(request, item_id):
    edit_item = get_object_or_404(RelatedItemsModel, pk=item_id)
    editedItem = RelatedItemsForm(request.POST or None, instance=edit_item)
    if editedItem.is_valid():
        editedItem.save()
        print(editedItem)
        return redirect('allEntries')
    return render(request, 'wikiApp/editRelatedItems.html', {'editedItem': editedItem}, {"item_id": item_id})


# Delete the item related to an entry
def deleteRelatedItems(request, delete_item):
    delete_item = get_object_or_404(RelatedItemsModel, pk=delete_item)
    if request.method == 'POST':
        delete_item.delete()
        print(delete_item)
        return redirect('allEntries')
    return render(request, 'wikiApp/deleteRelatedItems.html', {"delete_item": delete_item})


# find informations through the search bar
def search(request):
    makeSearch = request.POST['mySearch']
    research = PostModel.objects.filter(Q(post_Title__startswith=makeSearch))
    return render(request, 'wikiApp/search.html', {'research': research})
