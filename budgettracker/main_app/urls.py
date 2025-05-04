from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/',views.index, name='index'),
    path('add_expenses', views.add_expenses, name='add_expenses'),
]