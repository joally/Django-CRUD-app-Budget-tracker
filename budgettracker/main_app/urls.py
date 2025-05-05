from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import path



urlpatterns = [
    
    path('', views.expenses_view, name='expenses'), 
    path('about/', views.about, name='about'),
    path('index/',views.index, name='index'),
    path('expenses/', views.expenses_view, name='expenses'),
    path('add_expenses', views.add_expenses, name='add_expenses'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
