"""sharedlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from .views import *


urlpatterns = [

    path('add/<str:name>/', sharedlist_add),

    path('del/<str:name>/', sharedlist_del),

	path('<slug:list_slug>/add/<str:item_name>/', sharedlistitem_add),

	path('<slug:list_slug>/del/<str:item_name>/', sharedlistitem_del),

	path('<slug:list_slug>/<slug:item_slug>/mark-done/<int:done>/', sharedlistitem_mark_done),

	path('<slug:list_slug>/', sharedlist_detail),

    path('', sharedlist_detail),
]
