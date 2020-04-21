"""lost_found URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from info.views import (
    SiteList,
    ItemList,
    ItemDetail,
    SiteDetail,
    SiteCreate,
    ItemCreate,
)


urlpatterns = [
    path('item/',
         ItemList.as_view(),
         name = 'info_item_list_url_pattern'),
    path('item/<int:pk>/',
         ItemDetail.as_view(),
         name = 'info_item_detail_url_pattern'),
    path('item/create/',
         ItemCreate.as_view(),
         name='info_item_create_url_pattern'
         ),
    path('site/',
         SiteList.as_view(),
         name = 'info_site_list_url_pattern'),
    path('site/<int:pk>/',
         SiteDetail.as_view(),
         name = 'info_site_detail_url_pattern'),
    path('site/create/',
         SiteCreate.as_view(),
         name = 'info_site_create_url_pattern'
         ),
]
