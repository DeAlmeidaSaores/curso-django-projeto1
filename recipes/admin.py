from django.contrib import admin

from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

#@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Recipe, RecipeAdmin)
#ou @admin.register(Recipe) só que em cima da class Recipe
admin.site.register(Category, CategoryAdmin)
#ou @admin.register(Category)
 