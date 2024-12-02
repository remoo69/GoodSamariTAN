# models.py
from django.db import models

class DonationForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    height = models.IntegerField()  
    width = models.IntegerField()    
    weight = models.IntegerField()  
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='donations/', null=True, blank=True)

    def __str__(self):
        return self.name
