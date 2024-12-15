from django.contrib import admin

# Register your models here.
from .models import DonationForm, NGO, NGOGallery, NGOCategory, Message, Subscriber

admin.site.register(DonationForm)
admin.site.register(NGO)
admin.site.register(NGOGallery)
admin.site.register(NGOCategory)
admin.site.register(Message)
admin.site.register(Subscriber)