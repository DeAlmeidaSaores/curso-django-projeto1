from django.urls import path 
from . import views


app_name = 'recipes' #serve para criar um namespace com código mais bontio


urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:id>/', views.recipe, name="recipe"),

]
