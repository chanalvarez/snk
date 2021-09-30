from django.db import models
from django.contrib.auth.models import User




class Account(models.Model):
    user = models.OneToOneField(User,null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200 , null = True)
    email = models.EmailField(max_length= 200, null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return str(self.user)


class Playlist(models.Model):
    title = models.CharField(max_length= 200)
    fav = models.BooleanField(default = False)
    tag = models.CharField(max_length= 40)
    description = models.CharField(max_length= 2000)
    link = models.CharField(max_length=2000 , default='Add link here') 
    pic = models.ImageField(null = True , blank = True)
    account = models.ForeignKey(Account, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=200 , default= 'title')
    status = models.BooleanField(default= False)
    account = models.ForeignKey(Account, null = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.title

class Brand(models.Model):
    Name = models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class Shoes(models.Model):
    title = models.CharField(max_length= 200)
    status = models.BooleanField(default=False)
    size = models.CharField(max_length= 40)
    description = models.CharField(max_length= 2000)
    brand = models.ForeignKey(Brand, null = True, on_delete = models.SET_NULL)
    prize = models.IntegerField(max_length=999)
    pic = models.ImageField(null = True , blank = True)
    account = models.ForeignKey(Account, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.title