from django.urls import path
from StaticApp import views2

urlpatterns = [
    path(r'',views2.index),
]
