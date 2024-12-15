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



class Ngo(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    about_us=models.TextField()
    slug=models.SlugField()

    def __str__(self):
        return self.name
    
class NgoImage(models.Model):
    ngo=models.ForeignKey(Ngo, on_delete=models.CASCADE, related_name="images")
    image=models.ImageField(upload_to="media/ngo")

class NgoNeeded(models.Model):
    ngo=models.ForeignKey(Ngo, on_delete=models.CASCADE, related_name="needed")
    name=models.CharField(max_length=100)

class NgoDonationMethod(models.Model):
    ngo=models.ForeignKey(Ngo, on_delete=models.CASCADE, related_name="donation_method")
    method=models.CharField(max_length=30)
    number_or_link=models.CharField(max_length=40)    