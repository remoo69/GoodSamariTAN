# GoodSamariTAN/urls.py
from django.contrib import admin
from django.urls import path, include
from application import views  # Ensure "application" is your app's name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donation_form/', views.donation_view, name='donation_form'),
    path('', views.landing_page, name='landing_page'),
    path('', views.landingPage, name='home'),  # Set landingPage as home
    
    path('apply-ngo/', views.ngo_application, name='ngo_application'),
    path('login/', views.login_view, name='login'),
    path('ngo-application-submit/', views.ngo_application_submit, name='ngo_application_submit'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('check_unique/', views.check_unique, name='check_unique'),
    
    path('logout/', views.logout_view, name='logout'),
    
    path('', views.ngos_view, name='ngos_view'),  # Root URL now points to ngos_view
    path('ngos/', views.ngos_view, name='ngos_view'),  # Optional: Keep this if needed
    path('search_ngos/', views.search_ngos, name='search_ngos'), 
    
     path('', views.landing_page_view, name='home'),   
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
