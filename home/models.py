from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'images/', default='default.jpg', blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Preparation(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'images/', default='default.jpg', blank=True, null=True)
    recipe = models.TextField()
    duration= models.CharField(max_length=20)
    prep = models.TextField()
    method = models.CharField(max_length=30)
    utensils = models.TextField()
    procedure = models.TextField()
    plating = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.method


    











