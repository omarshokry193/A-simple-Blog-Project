from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
# Create your models here.
class Category(models.Model):
    name =        models.CharField(max_length=255, default='Coding')
    def __str__(self):
        return self.name
    def get_absolute_url(self): 
        return reverse('core:home')
class Post(models.Model):
    title =       models.CharField(max_length=255)
    snippet = models.CharField(max_length=300)
    author =      models.ForeignKey(User,on_delete=models.CASCADE)
    body =        models.TextField()
    post_date =   models.DateField(auto_now_add = True)
    category =    models.CharField(max_length=255, default='Coding')
    likes = models.ManyToManyField(User,related_name='blog_post')

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('core:article-detail', args=[str(self.id)])
    

class Comment(models.Model):
    post =      models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name =      models.CharField(max_length=300)
    comment =      models.TextField()
    date_added =    models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)