from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase


#reverse pega o nome que você deu á URL e descobre qual o caminho dela como string
#Esse objects é um objeto responsável por fazer a comunicação entre o seu código Python e os registros do banco de dados.
class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self): #TESTA QUAL FUNÇÃO ESTÁ LIGAGA A URL
        view = resolve(
            reverse('recipes:home')
        ) #criando um objeto
        self.assertIs(view.func, views.home) #view.func pq a view é uma função. O objeto view criando acima nao me retorna uma view, me retorna um objeto com outras informações o uso do view.func limita essa comparação de informação
            #IMPORTANTE: o IS verifica a identidade, ou seja, se as duas referencias apotam para o mesmo objeto na memória
      
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home')) #client.get é um obejto Client que o TestCase cria. Ele serve pra simular um navegador fazendo requisições
        self.assertEqual(response.status_code, 200) #verifica se o status code é 200 = ok

    def test_recipe_home_view_loods_correct_(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here! </h1>',
            response.content.decode('utf-8') 
        ) 
     
    def test_recipe_home_template_loads_recipes(self): #O Django cria um banco de dados separado para os testes.
        
        self.make_recipe() #aqui to criando uma receita 

        response = self.client.get(reverse('recipes:home')) #Faça uma requisição GET para a URL que corresponde a recipes:home.
        content = response.content.decode('utf-8') #pega o HTML que veio na resposta e transforma em texto
        response_context_recipes = response.context['recipes'] #pega pela chave de context e vereficia se tem apenas uma receita criada(quando for testado)


        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self): 
        """
            Testa quando (is_publish=Falso) não é exibido receitas não publicadas'. 
        """
        self.make_recipe(is_published=False) 

        response = self.client.get(reverse('recipes:home')) 
        content = response.content.decode('utf-8') 
        
        self.assertIn(
            '<h1>No recipes found here! </h1>',
            response.content.decode('utf-8') 
        ) 
    
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id':1000})
        ) 
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id':1000})
        ) 
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipes(self): 
            need_title = 'This is a detail page - It load one recipe' 

            self.make_recipe(title=need_title) 
            response = self.client.get(
                 reverse(
                      'recipes:recipe',
                      kwargs={
                           'id' : 1
                      }
                    )
                ) 
            content = response.content.decode('utf-8') 
    
            self.assertIn(need_title, content)
   
    def test_recipe_category_template_dont_load_recipes_not_published(self): 

        recipe = self.make_recipe(is_published=False) 

        response = self.client.get(reverse('recipes:category', kwargs={'category_id' : recipe.category.id})) 

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe' , kwargs={'id': 1})
        ) 
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
            response = self.client.get(
                reverse('recipes:recipe' , kwargs={'id': 1000})
                ) 
            self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_dont_load_recipe_not_published(self): 
        recipe = self.make_recipe(is_published=False) 

        response = self.client.get(reverse('recipes:recipe', kwargs={'id' : recipe.id})) 

        self.assertEqual(response.status_code, 404)