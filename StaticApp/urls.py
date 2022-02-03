from django.urls import path
from StaticApp import views

urlpatterns = [
    path(r'',views.index),
]
