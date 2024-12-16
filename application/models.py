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
    height = models.IntegerField(null=True, blank=True)  # Make optional
    width = models.IntegerField(null=True, blank=True)   # Make optional
    weight = models.IntegerField(null=True, blank=True)  # Make optional
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='donations/', null=True, blank=True)
    ngo = models.ForeignKey('NGO', on_delete=models.CASCADE)  # Link to NGO

    def __str__(self):
        return f"{self.name} - {self.ngo.name}"

class NGO(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='ngos/covers/')
    about = models.TextField()
    needs = models.TextField()  # Store as a comma-separated list
    city = models.CharField(max_length=255)
    exact_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    other_donation_methods = models.TextField()
    gallery = models.ManyToManyField('NGOGallery')
    categories = models.ManyToManyField('NGOCategory')
    verified = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return self.name

class NGOGallery(models.Model):
    image = models.ImageField(upload_to='ngos/gallery/')

    def __str__(self):
        return f"Gallery Image {self.id}"

class NGOCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email