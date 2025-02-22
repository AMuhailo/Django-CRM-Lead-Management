"""
URL configuration for crmsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from lead.views import HomeTemplateView, SinginView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sing-in/',SinginView.as_view(), name = 'singin'),
    path('login/',auth_view.LoginView.as_view(), name = 'login'),
    path('logout/',auth_view.LogoutView.as_view(), name = 'logout'),
    path('',HomeTemplateView.as_view(), name = 'home_template_url'),
    path('admin/', admin.site.urls),
    path('lead/',include('lead.urls', namespace='lead')),
    path('agent/',include('agent.urls')),
    path('__debug__/',include('debug_toolbar.urls'))
]
