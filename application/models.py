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
    
class NGOApplication(models.Model):
    ein = models.CharField(max_length=15, unique=True)  # Ensures EIN is unique
    name = models.CharField(max_length=255, unique=True)  # Ensures name is unique
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Ensures email is unique
    password = models.CharField(max_length=128)
    form_990 = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name