from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User#user table
from django.urls import reverse  #reverse will return the full URL to the route as a string and let the view handle redirect 

# Create your models here.
#users and posts

class Post(models.Model): #post class inherits from model.Model, each class is it's own table in DB
    title= models.CharField(max_length=100) #each attribute is a different field in DB
    date_posted= models.DateTimeField(default= timezone.now) #we do not execute the function, we just pass in the function as actual value
    author=models.ForeignKey(User,on_delete=models.CASCADE ) # user and model have a 1-many relationship, as one user can have many posts, we use a foreign key, delete the post when user is deleted
    content= models.TextField()

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) #will return full path as a string








