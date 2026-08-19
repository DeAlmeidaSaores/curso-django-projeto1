from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe



def home(request): #importante saber que aqui o meu objeto se chama recipe
    recipes = Recipe.objects.all().order_by('-id') #aqui eu instanciel o recipe por isso posso usar o recipe.cover no for com recipe
    return render(request, 'recipes/pages/home.html', context={
    'recipes' : recipes,
})


def Category(request, category_id): 
    recipes = Recipe.objects.filter(
        category__id=category_id
        ).order_by('-id') 
    return render(request, 'recipes/pages/home.html', context={
    'recipes' : recipes,
})



def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context=
    {'recipe' : make_recipe,
     'is_detail_page' : True,
})








  