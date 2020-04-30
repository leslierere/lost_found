from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from info.forms import SiteForm, ItemForm
from info.utils import PageLinksMixin
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

class ItemList(PageLinksMixin, ListView):
    paginate_by = 10
    model = Item

# class ItemList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'info/item_list.html',
#             {'item_list': Item.objects.all()}
#         )


class ItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            Item,
            pk=pk
        )
        return render(
            request,
            'info/item_detail.html',
            {'item': item}
        )


class ItemCreate(CreateView):
    form_class = ItemForm
    model = Item


class ItemUpdate(UpdateView):
    form_class = ItemForm
    model = Item
    template_name = 'info/item_form_update.html'



class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('info_item_list_urlpattern')



class SiteList(PageLinksMixin, ListView):
    paginate_by = 15
    model = Site


class SiteDetail(View):

    def get(self, request, pk):
        site = get_object_or_404(
            Site,
            pk=pk
        )
        return render(
            request,
            'info/site_detail.html',
            {'site': site}
        )


class SiteCreate(CreateView):
    form_class = SiteForm
    model = Site


class SiteUpdate(UpdateView):
    form_class = SiteForm
    model = Site
    template_name = 'info/site_form_update.html'


class SiteDelete(View):

    def get(self, request, pk):
        site = self.get_object(pk)
        items = site.items.all()
        if items.count() > 0:
            return render(
                request,
                'info/site_refuse_delete.html',
                {'site': site,
                 'items': items}
            )
        else:
            return render(
                request,
                'info/site_confirm_delete.html',
                {'site': site}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Site,
            pk=pk
        )

    def post(self, request, pk):
        site = self.get_object(pk)
        site.delete()
        return redirect('info_site_list_urlpattern')
