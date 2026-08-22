from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import Recipe



def home(request): #importante saber que aqui o meu objeto se chama recipe
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id') #aqui eu instanciel o recipe por isso posso usar o recipe.cover no for com recipe
    return render(request, 'recipes/pages/home.html', context={
    'recipes' : recipes, # o 1 recipes é o nome do template
                        # o 2 recipes é a variável com todas as receitas 
})


def Category(request, category_id): 
    recipes = Recipe.objects.filter( #aqui se forma a QuerySet
        category__id=category_id,#__ serve pra pegar o dado de category, ele ta no model recipe acessando através da foreingkey
        is_published=True, 
        ).order_by('-id') 

    if not recipes: #preocura recipes se não econtrar retorne isso
        raise Http404('Not Found')

    return render(request, 'recipes/pages/category.html', context={
    'recipes' : recipes,
    'title' : f'{recipes.first().category.name }- Category ' #isso aqui ele pega dentro da QuerySet selecionado passo a passo. Então eu tenho no final uma string com um name Do model Category


})



def recipe(request, id):
   recipe = Recipe.objects.filter(
       pk=id,
       is_published=True,
    ).order_by('-id').first()

   return render(request, 'recipes/pages/recipe-view.html', context={
    'recipe': recipe,
    'is_detail_page': True
   })









  