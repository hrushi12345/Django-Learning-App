from django.urls import path
from TemplateApp import views

urlpatterns = [
    path(r'',views.index),
]
