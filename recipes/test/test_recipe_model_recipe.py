from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase




class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None :
        self.recipe = self.make_recipe()
        return super().setUp() # o super() diz: além do que eu fiz no meu setUp(), execute também o setUp() que veio do pai (TasteCase)

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError): #assertRaises() → método que retorna um Context Manager
        # With diz qual codigo o assertRaises vai encontrar o erro
            self.recipe.full_clean() #serve para validar um objeto de model antes de salvar

    def test_recipe_fields_max_length(selff):
        fiedls = [
            ('title', 65), 
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings', 65),
        ]

        for field, max_length in fiedls:
            setattr(self.recipe, field, 'A' * (max_length + 0)) #a cada rodada é como se self.recipe.title = 'AAAA...'
           
            with self.assertRaises(ValidationError):
                self.recipe.full_clean()

    