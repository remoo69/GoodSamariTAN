from django.contrib import admin

# Register your models here.
from .models import DonationForm, NGOApplication

admin.site.register(DonationForm)

@admin.register(NGOApplication)
class NGOApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'ein', 'email', 'created_at')
    search_fields = ('name', 'ein', 'email')
    list_filter = ('created_at',)
