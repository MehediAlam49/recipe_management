
from django.contrib import admin
from django.urls import path
from recipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('', home, name='home'),
    path('addRecipe/', addRecipe, name='addRecipe'),
    path('editRecipe/', editRecipe, name='editRecipe'),
    path('viewRecipe/', viewRecipe, name='viewRecipe'),
    path('deleteRecipe/', deleteRecipe, name='deleteRecipe'),
]
