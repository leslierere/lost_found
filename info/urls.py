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
    LostItemList,
    LostItemDetail,
    LostItemCreate,
    LostItemUpdate,
    LostItemDelete,
    FoundItemList,
    FoundItemDetail,
    FoundItemCreate,
    FoundItemUpdate,
    FoundItemDelete,
    SiteDetail,
    SiteCreate,
    SiteUpdate,
    SiteDelete,
)


urlpatterns = [
    # path('item/',
    #      ItemList.as_view(),
    #      name = 'info_item_list_urlpattern'),
    # path('item/found/',
    #      FoundItems.as_view(),
    #      name='info_item_found_urlpattern'),
    path('item/lost/',
         LostItemList.as_view(),
         name='info_item_list_lost_urlpattern'),
    path('item/lost/<int:pk>/',
         LostItemDetail.as_view(),
         name = 'info_item_detail_lost_urlpattern'),
    path('item/lost/create/',
         LostItemCreate.as_view(),
         name='info_item_create_lost_urlpattern'
         ),
    path('item/lost/<int:pk>/update/',
         LostItemUpdate.as_view(),
         name='info_item_update_lost_urlpattern'
         ),
    path('item/lost/<int:pk>/delete/',
         LostItemDelete.as_view(),
         name='info_item_delete_lost_urlpattern'
         ),
    path('item/found/',
         FoundItemList.as_view(),
         name='info_item_list_found_urlpattern'),
    path('item/found/<int:pk>/',
         FoundItemDetail.as_view(),
         name='info_item_detail_found_urlpattern'),
    path('item/found/create/',
         FoundItemCreate.as_view(),
         name='info_item_create_found_urlpattern'
         ),
    path('item/found/<int:pk>/update/',
         FoundItemUpdate.as_view(),
         name='info_item_update_found_urlpattern'
         ),
    path('item/found/<int:pk>/delete/',
         FoundItemDelete.as_view(),
         name='info_item_delete_found_urlpattern'
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
    path('site/<int:pk>/update/',
         SiteUpdate.as_view(),
         name='info_site_update_urlpattern'),
    path('site/<int:pk>/delete/',
         SiteDelete.as_view(),
         name='info_site_delete_urlpattern'
         ),
]
