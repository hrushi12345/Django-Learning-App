from django.urls import path
from RegistrationApp import views2

# TEMPLATE URLS!
app_name = 'RegistrationApp'

urlpatterns = [
    path('index/',views2.index, name='index'),
    path('register/', views2.register, name='register'),
    path('login/', views2.user_login, name='login'),
]
#     
