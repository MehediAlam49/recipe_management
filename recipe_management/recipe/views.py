from django.shortcuts import render, redirect, HttpResponse
from recipe.models import *

# Create your views here.
# <------------Authentication---------------->
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return render(request, 'logoutPage.html')



# <------------CRUD---------------->
def home(request):
    return render(request, 'home.html')
def addRecipe(request):
    return render(request, 'addRecipe.html')
def editRecipe(request):
    return render(request, 'editRecipe.html')
def viewRecipe(request):
    return render(request, 'viewRecipe.html')
def deleteRecipe(request):
    return render(request, 'deleteRecipe.html')