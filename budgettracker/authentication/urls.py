from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_login/', views.my_login, name='my_login'),  
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    

]