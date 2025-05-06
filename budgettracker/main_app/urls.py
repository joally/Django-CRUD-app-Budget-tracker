from django.urls import path, include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView





urlpatterns = [
    
    path('', views.expenses_view, name='expenses'), 
    
    path('authentication/', include('authentication.urls')),


    path('about/', views.about, name='about'),
    
   
    path('add_expenses/', views.add_expenses, name='add_expenses'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
