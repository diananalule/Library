from django.db import models



    
class Book(models.Model):
    title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now_add=True) 
    Publication_date=models.DateField()
    Subject_area=models.CharField(max_length=100)
    
    
    
    
    
    
    
    
