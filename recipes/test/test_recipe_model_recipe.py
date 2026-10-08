from django.core.exceptions import ValidationError
from .test_recipe_base import RecipeTestBase, Recipe
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None :
        self.recipe = self.make_recipe()
        return super().setUp() # o super() diz: além do que eu fiz no meu setUp(), execute também o setUp() que veio do pai (TasteCase)

    def make_recipe_no_defaults(self):
        recipe = Recipe(
                category=self.make_category(name='Test Default Category'),
                author=self.make_author(username='newuser'),
                title='Recipe Title',
                description='Recipe Description',
                slug='recipe-slug',
                preparation_time=10,
                preparation_time_unit='Minutos',
                servings=5,
                servings_unit='Porções',
                preparation_steps='Recipe Preparation Steps',         
            )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([ #Parametrização: fazer um mesmo teste receber diferentes valores de entrada, 
                            #sem precisar criar um teste separado para cada valor.
        ('title', 65),      #O expand é o que faz o teste ser expandido em várias execuções, uma para cada tupla da lista.
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError): 
            #assertRaises() → método que retorna um Context Manager
            # With diz qual bloco de codigo o assertRaises vai encontrar o erro
            self.recipe.full_clean() 
            #serve para validar um objeto de model antes de salvar. 
            #Pq as vezes passa e salva com erros sem validar
            
    
    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
            recipe = self.make_recipe_no_defaults()
            self.assertFalse(recipe.preparation_steps_is_html)
            
            
    def test_recipe_is_published_is_false_by_default(self): 
        #Esse teste verifica qual é o valor padrão de is_published,
        #quando uma receita é criada sem informar esse campo.
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published)


    def test_recipe_string_representation(self):
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), 'Testing Representation')
        #str() chama o __str__ do objeto
        #Ou seja, transforma o objeto em string