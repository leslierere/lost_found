from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from info.forms import SiteForm, LostItemForm, FoundItemForm
from info.utils import PageLinksMixin
from .models import (
    LostItem,
    FoundItem,
    Site)


# Create your views here.
# def item_list_view(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('info/item_list.html')
#     context = {'item_list': item_list}
#     output = template.render(context)
#     return HttpResponse(output)

# class ItemList(PageLinksMixin, ListView):
#     paginate_by = 10
#     model = Item

# class ItemList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'info/item_list.html',
#             {'item_list': Item.objects.all()}
#         )

class LostItemList(PageLinksMixin, ListView):
    paginate_by = 10
    model = LostItem
    context_object_name = 'lost_items_list'




class LostItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            LostItem,
            pk=pk
        )
        return render(
            request,
            'info/item_detail_lost.html',
            {'item': item}
        )


class LostItemCreate(CreateView):
    form_class = LostItemForm
    model = LostItem


class LostItemUpdate(UpdateView):
    form_class = LostItemForm
    model = LostItem
    template_name = 'info/item_form_update.html'



class LostItemDelete(DeleteView):
    model = LostItem
    success_url = reverse_lazy('info_item_list_lost_urlpattern')


class FoundItemList(PageLinksMixin, ListView):
    paginate_by = 10
    model = FoundItem
    context_object_name = 'found_items_list'

# class FoundItems(PageLinksMixin, ListView):
#     paginate_by = 10
#     model = FoundItem
#     # context_object_name = 'found_item_list'


class FoundItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            FoundItem,
            pk=pk
        )
        return render(
            request,
            'info/item_detail_found.html',
            {'item': item}
        )


class FoundItemCreate(CreateView):
    form_class = FoundItemForm
    model = FoundItem


class FoundItemUpdate(UpdateView): # duplicates
    form_class = FoundItemForm
    model = FoundItem
    template_name = 'info/item_form_update.html'



class FoundItemDelete(DeleteView): # duplicates
    model = FoundItem
    success_url = reverse_lazy('info_item_list_found_urlpattern')
    # context_object_name = 'item'



class SiteList(PageLinksMixin, ListView):
    paginate_by = 15
    model = Site


class SiteDetail(View):

    def get(self, request, pk):
        site = get_object_or_404(
            Site,
            pk=pk
        )
        item_list = site.items.all()
        return render(
            request,
            'info/site_detail.html',
            {'site': site, 'item_list':item_list}
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
