from django.urls import path
from TemplateApp import views1

urlpatterns = [
    path(r'',views1.index),
]
