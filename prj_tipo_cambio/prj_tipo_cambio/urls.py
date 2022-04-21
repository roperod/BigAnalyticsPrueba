"""prj_tipo_cambio URL Configuration

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
from django.urls import path

from tipo_cambio.views import add, show, update, delete
from accounts.views import user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_login),
    path('accounts/<page>/', show),
    path('login/', user_login),
    path('logout/', user_logout),
    path('', show),
    path('show/', show),
    path('add/', add),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
]
