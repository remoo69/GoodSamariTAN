# GoodSamariTAN/urls.py
from django.contrib import admin
from django.urls import path
from application import views  # Ensure "application" is your app's name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donation_form/', views.donation_view, name='donation_form'),
    path('about/', views.about_page, name='about'),
    path('ngo/<slug:ngo_slug>/', views.about_page, name='ngo_detail'),
    path('', views.landing_page, name='landing_page'),
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
