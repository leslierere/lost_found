from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader


from .models import (
    Item,
    Site)

# Create your views here.
def item_list_view(request):
    item_list = Item.objects.all()
    template = loader.get_template('info/item_list.html')
    context = {'item_list': item_list}
    output = template.render(context)
    return HttpResponse(output)

def site_list_view(request):
    site_list = Site.objects.all()
    template = loader.get_template('info/site_list.html')
    context = {'site_list': site_list}
    output = template.render(context)
    return HttpResponse(output)