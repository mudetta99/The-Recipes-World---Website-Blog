from django.db import models


# Website Models

class Recipes(models.Model):

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    popular = models.BooleanField(default=True,null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    added_at = models.DateTimeField(auto_now_add=True)


class Recipes_opinion(models.Model):
    user = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    recipeId = models.CharField(max_length=11, null=True)
    recipeName = models.CharField(max_length=250, null=True)
    opinion = models.TextField(max_length=2000, null=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True)


class Contact_us(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    added_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)



# Blog Models
    
class BlogRecipes(models.Model):

    name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=300, null=True)
    description = models.TextField(null=True)
    country = models.CharField(max_length=100, null=True, default='none')
    active = models.BooleanField(default=True, null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(null=True, max_length=50)


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    added_at = models.DateTimeField(auto_now_add=True)


