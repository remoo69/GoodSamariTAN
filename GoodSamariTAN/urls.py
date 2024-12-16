# GoodSamariTAN/urls.py
from django.contrib import admin
from django.urls import path, include
from application import views  # Ensure "application" is your app's name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donation_form/', views.donation_view, name='donation_form'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ngos/', views.ngo_list, name='ngo_list'),
    path('ngos/<int:pk>/', views.ngo_detail, name='ngo_detail'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('apply-ngo/', views.ngo_application, name='ngo_application'),
    path('apply-ngo/submit/', views.ngo_application_submit, name='ngo_application_submit'),
] 

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
