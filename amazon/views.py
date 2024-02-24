from django.shortcuts import render, get_object_or_404
from .models import Recipes, BlogRecipes, Blogs, Contact_us, Recipes_opinion


def index(request):
    # Show newest recipes in the website
    newest_recipes = Recipes.objects.filter(active = True)[:4]

    # Show popular recipes in the website
    popular_recipes = Recipes.objects.filter(popular = True)[:4]

    # Show upcoming recipes in the website
    upcoming_recipes = Recipes.objects.filter(active = False)

    # Show Blogs in the website
    blogs_in_website = Blogs.objects.all().order_by('-added_at')[:2]

    # Contact_us
    # contact_name = request.POST.get('name')
    # contact_email = request.POST.get('email')
    # contact_message = request.POST.get('message')

    # data = Contact_us(name=contact_name, email=contact_email, message=contact_message)
    # data.save()

    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_message = request.POST.get('message')

        # Check if any of the required fields is empty
        if not contact_name or not contact_email or not contact_message:
            error_message = "All fields are required. Please fill out the form completely."
            
        # If all fields are provided, create and save the Contact_us instance
        data = Contact_us(name=contact_name, email=contact_email, message=contact_message)
        data.save()

    context = {
        'newest_recipes':newest_recipes,
        'upcoming_recipes':upcoming_recipes,
        'blogs_in_website':blogs_in_website,
        'popular_recipes':popular_recipes,
    }
    return render(request, 'amazon/index.html', context)


# About the website 
def about(request):
    return render(request, 'amazon/about.html')

# Show recipe details in the website
def recipe_details(request, recipe_name ,recipe_id):
    recipe = get_object_or_404(Recipes, name=recipe_name ,pk = recipe_id)
    # Users Opinions
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_id = request.POST.get('recipe_id')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_opinion = request.POST.get('user_opinion')

        if not recipe_name or not recipe_id or not user_name or not user_email or not user_opinion:
            error_message = "All fields are required. Please fill out the form completely."
        

        opinion = Recipes_opinion(recipeName=recipe_name, recipeId=recipe_id, user=user_name, email=user_email, opinion=user_opinion)
        opinion.save()

    context = {
        'recipe':recipe,
        'opinion_id':Recipes_opinion.objects.all(),
        'recipe_id':Recipes.objects.all()
    }

    return render(request, 'amazon/recipe_details.html', context)

# Show latest 3 blogs in the blog
def blog(request):
    recipes = BlogRecipes.objects.all().order_by('-added_at')[:3]
    return render(request, 'blog/index.html', {'recipes':recipes})

# Add Recipe in the blog 
def add_recipe(request):
    recipe_name        = request.POST.get('name')
    recipe_details     = request.POST.get('details')
    recipe_description = request.POST.get('description')
    recipe_country     = request.POST.get('country')
    recipe_image       = request.POST.get('image')
    recipe_publisher   = request.POST.get('publisher')

    data = BlogRecipes(name=recipe_name, details=recipe_details, description=recipe_description, country=recipe_country, image=recipe_image, publisher=recipe_publisher)
    data.save()

    return render(request, 'blog/add_recipe.html')

# Recipe Details in the blog
def blog_recipe_details(request, recipe_name, recipe_id):
    recipe = get_object_or_404(BlogRecipes, name=recipe_name, id=recipe_id)
    return render(request, 'blog/recipe_details.html', {'recipe':recipe})

# Show blogs in the blog
def blogs(request):
    blogs = Blogs.objects.order_by('-added_at')[:3]
    return render(request, 'blog/blogs.html', {'blogs':blogs})

# Show blogs Details in the blog
def blog_details(request, blog_title, blog_id):
    blog_details = get_object_or_404(Blogs, title=blog_title, id=blog_id)
    return render(request, 'blog/blog_details.html', {'blog_details':blog_details})






