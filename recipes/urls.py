from django.urls import path 
from . import views


app_name = 'recipes' #serve para criar um namespace com código mais bontio


urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.Category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    #aqui temos:
    # 1- URL que o site acessa
    # 2- View que vai atender a essa URL
    # 3- Da um nome intenro a minha URL, para que não precise escrever o caminho
]
