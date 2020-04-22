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
    ItemUpdate,
)


urlpatterns = [
    path('item/',
         ItemList.as_view(),
         name = 'info_item_list_urlpattern'),
    path('item/<int:pk>/',
         ItemDetail.as_view(),
         name = 'info_item_detail_urlpattern'),
    path('item/create/',
         ItemCreate.as_view(),
         name='info_item_create_urlpattern'
         ),
    path('item/update/',
         ItemUpdate.as_view(),
         name='info_item_update_urlpattern'
         ),
    path('site/',
         SiteList.as_view(),
         name = 'info_site_list_urlpattern'),
    path('site/<int:pk>/',
         SiteDetail.as_view(),
         name = 'info_site_detail_urlpattern'),
    path('site/create/',
         SiteCreate.as_view(),
         name = 'info_site_create_urlpattern'
         ),
]
