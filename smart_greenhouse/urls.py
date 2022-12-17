"""smart_greenhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('user/<str:s>', views.user, name='user'),
    path('user/<str:s>/add_greenhouse', views.user_add_greenhouse, name='add_greenhouse'),
    path('greenhouse/register', views.register_greenhouse, name='register_greenhouse'),
    path('greenhouse/<str:id>', views.get_greenhouse, name='get_greenhouse'),
    path('greenhouse/<str:id>/state', views.greenhouse_state, name='greenhouse_state'),
    path('greenhouse/<str:id>/history', views.greenhouse_history, name='greenhouse_history'),
    path('greenhouse/<str:id>/history/add', views.greenhouse_history_add, name='greenhouse_history_add'),
]