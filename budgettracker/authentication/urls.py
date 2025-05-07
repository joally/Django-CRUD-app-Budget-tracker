from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_login/', views.my_login, name='my_login'),  
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.create_record, name='create-record'),
    path('record/<int:pk>', views.singular_record, name='record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),
    

]