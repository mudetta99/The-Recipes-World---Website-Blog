from django.urls import path
from . import views


urlpatterns = [

    # Website urls
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('recipe/<str:recipe_name>/<int:recipe_id>', views.recipe_details, name='recipe_details'),

    # Blog urls
    path('blog', views.blog, name='blog'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('blog_recipe/<str:recipe_name>/<int:recipe_id>', views.blog_recipe_details, name='blog_details'),
    path('blogs', views.blogs, name='blogs'),
    path('<str:blog_title>/<int:blog_id>', views.blog_details, name='blog_details')
    
]


