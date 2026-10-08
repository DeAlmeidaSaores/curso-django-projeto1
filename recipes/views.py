from django.http import Http404
from django.shortcuts import get_list_or_404, render
from utils.recipes.factory import make_recipe

from .models import Recipe
#OBS: NÃO USEI O get_list_or_404 nas outras funções pq eu não quis


def home(request): #importante saber que aqui o meu objeto se chama recipe
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id') #aqui  pega somente as receitas publicadas 
    
    return render(request, 'recipes/pages/home.html', context={
    'recipes': recipes, # o 1 recipes é o nome do template vai usar la na pasta do template
                        # o 2 recipes é a variável com todas as receitas 
})


def category(request, category_id): 
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
       pk=id, #pk é o primarykey (procure a Recipe cuja chave primária seja igual ao valor que recevi na variável id)
       is_published=True,
    ).order_by('-id').first()

   if not recipe: #preocura recipes se não econtrar retorne isso
           raise Http404('Not Found')

   return render(request, 'recipes/pages/recipe-view.html', context={
    'recipe': recipe,
    'is_detail_page': True
   })










  