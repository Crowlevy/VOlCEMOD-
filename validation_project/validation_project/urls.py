from django.urls import path
from django.contrib import admin
from app_user import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('Angola_Hub/', views.Angola_Hub, name = 'Angola_Hub'),
    path('admin/', admin.site.urls),
    
]
