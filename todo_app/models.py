from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Third party packets
from autoslug import AutoSlugField

class Category(models.Model):
    title=models.CharField(max_length=30)
    slug=AutoSlugField(populate_from='title',unique=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'category_view',
            kwargs={
                'slug_category':self.slug,
            }            
        )

class Tag(models.Model):
    title=models.CharField(max_length=30)
    slug=AutoSlugField(populate_from='title',unique=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            'tag_view',
            kwargs={
                'slug_tag':self.slug,                
            }
        )


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #baris2= fjdkjsdl57348758
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)  # bunu kullanmıyoruz,category silinice todolar da silinir.
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tag=models.ManyToManyField(Tag)
    title= models.CharField(max_length=200)
    content=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Todo {str(self.id)} : {self.title}, user : {self.user} "

    def get_absolute_url(self):
        return reverse(
            'todo_detail',
            kwargs={
                'slug_category':self.category.slug,
                'id':self.id,
            }            
        )