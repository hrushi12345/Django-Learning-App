"""ProjectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import TemplateApp
# import StaticApp
from FormApp import views3
from RegistrationApp import views4

urlpatterns = [
    path(r"", views4.index, name="index"),  # Home page
    path("TemplateApp/", include("TemplateApp.urls")),
    path("StaticApp/", include("StaticApp.urls")),
    path("FormApp/", views3.formView, name="FormApp"),
    path("RegistrationApp/", include("RegistrationApp.urls")),
    path("logout/", views4.user_logout, name="logout"),
    path("admin/", admin.site.urls),
]
