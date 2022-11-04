from django.contrib.auth.models import AbstractUser,User
from django.db import models
from datetime import datetime,date
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return self.username


        
class category(models.Model):
    name = models.CharField(max_length=64)   
    def __str__(self):
        return self.name





class listing(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=64)
    des = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image= models.ImageField(upload_to="photo/%y/%m/%d",blank=True,null=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())
    



    def __str__(self):
        return self.title
    

class Bid(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    listing=models.ForeignKey(listing,on_delete=models.CASCADE,blank=True,null=True)
    start = models.DecimalField(max_digits=8, decimal_places=2)
    win = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())
    


    def __str__(self):
        return str(self.User)
    
class watchlist(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    listing=models.ForeignKey(listing,on_delete=models.CASCADE,blank=True,null=True)

class comment(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    listing=models.ForeignKey(listing,on_delete=models.CASCADE,blank=True,null=True)


    des = models.TextField()







