from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (
    Item,
    Site)

# Create your views here.
# def item_list_view(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('info/item_list.html')
#     context = {'item_list': item_list}
#     output = template.render(context)
#     return HttpResponse(output)

class ItemList(View):

    def get(self, request):
        return render(
            request,
            'info/item_list.html',
            {'item_list': Item.objects.all()}
        )

class ItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            Item,
            pk = pk
        )
        return render(
            request,
            'info/item_detail.html',
            {'item': item}
        )

class SiteList(View):

    def get(self, request):
        return render(
            request,
            'info/site_list.html',
            {'site_list': Site.objects.all()}
        )


class SiteDetail(View):

    def get(self, request, pk):
        site = get_object_or_404(
            Site,
            pk = pk
        )
        return render(
            request,
            'info/site_detail.html',
            {'site': site}
        )