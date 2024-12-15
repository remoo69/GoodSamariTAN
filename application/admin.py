from django.contrib import admin

# Register your models here.
from .models import DonationForm, NGO, NGOGallery, NGOCategory, Message, Subscriber, NGOCategory

admin.site.register(DonationForm)
admin.site.register(NGO)
admin.site.register(NGOGallery)
admin.site.register(Message)
admin.site.register(Subscriber)



class NGOCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_ngos')  # Display category name and associated NGOs
    
    def get_ngos(self, obj):
        ngos = obj.ngo_set.all()
        return ", ".join([ngo.name for ngo in ngos]) if ngos else "No NGOs"

    get_ngos.short_description = "Organizations"  
    
admin.site.register(NGOCategory, NGOCategoryAdmin)