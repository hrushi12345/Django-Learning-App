from django.urls import path
from RegistrationApp import views4

# TEMPLATE URLS!
app_name = 'RegistrationApp'

urlpatterns = [
    path('index/',views4.index, name='index'),
    path('register/', views4.register, name='register'),
    path('login/', views4.user_login, name='login'),
]
#     
