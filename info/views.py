from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from info.forms import SiteForm, ItemForm
from info.utils import ObjectCreateMixin
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


class ItemCreate(ObjectCreateMixin, View):
    form_class = ItemForm
    template_name = 'info/item_form.html'


class ItemUpdate(View):
    form_class = ItemForm
    model = Item
    template_name = 'info/item_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk
        )

    def get(self, request, pk):
        item = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=item),
            'item': item,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        item = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=item)
        if bound_form.is_valid():
            new_item = bound_form.save()
            return redirect(new_item)
        else:
            context = {
                'form': bound_form,
                'item': item,
            }
            return render(
                request,
                self.template_name,
                context
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


class SiteCreate(ObjectCreateMixin, View):
    form_class = SiteForm
    template_name = 'info/site_form.html'


