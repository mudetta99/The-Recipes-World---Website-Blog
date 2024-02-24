from django.contrib import admin
from .models import Recipes, Recipes_opinion, BlogRecipes, Blogs, Contact_us

# Website
class RecipeDetails(admin.ModelAdmin):
    list_display = ('name', 'active')
admin.site.register(Recipes, RecipeDetails)


class RecipesOpinion(admin.ModelAdmin):
    list_display = ('user', 'recipeName', 'opinion', 'added_at')
admin.site.register(Recipes_opinion, RecipesOpinion)


class ContactUsDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'added_at')
admin.site.register(Contact_us, ContactUsDetails)


# Blog
class BlogRecipesDetails(admin.ModelAdmin):
    list_display = ('name', 'active', 'added_at')
admin.site.register(BlogRecipes, BlogRecipesDetails)


class BlogsDetails(admin.ModelAdmin):
    list_display = ('title','added_at')
admin.site.register(Blogs, BlogsDetails)

