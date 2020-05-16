from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from info.forms import SiteForm, LostItemForm, FoundItemForm, AdviceForm
from info.utils import PageLinksMixin
from .models import (
    LostItem,
    FoundItem,
    Site, Advice)


class LostItemList(PageLinksMixin, ListView):
    paginate_by = 10
    model = LostItem
    queryset = LostItem.objects.filter(found=False)
    context_object_name = 'lost_items_list'


class MyItems(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    # Specifying model = LostItem is shorthand for saying queryset = LostItem.objects.all()
    # queryset = LostItem.objects.filter(user= request)
    context_object_name = 'my_items'
    template_name = 'info/myitems_list.html'  # why, sometimes this need not be specified
    permission_required = 'info.add_lostitem'

    def get_queryset(self):
        return LostItem.objects.filter(user=self.request.user)


class LostItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            LostItem,
            pk=pk
        )
        return render(
            request,
            'info/lostitem_detail.html',
            {'item': item}
        )


class LostItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = LostItemForm
    # form_class.fields['email'].initial = request.user.email
    model = LostItem
    permission_required = 'info.add_lostitem'

    # fields = ('item_name', 'place', 'eventDate', 'eventTime', 'description', 'phone', 'email')

    def get_initial(self):
        email = self.request.user.email
        return {'email': email}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LostItemCreate, self).form_valid(form)


class LostItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = LostItemForm
    model = LostItem
    template_name = 'info/item_form_update.html'
    permission_required = 'info.change_lostitem'


class LostItemDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = LostItem
    success_url = reverse_lazy('info_myitem_list_urlpattern')
    permission_required = 'info.delete_lostitem'


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
            'info/founditem_detail.html',
            {'item': item}
        )


class FoundItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = FoundItemForm
    model = FoundItem
    permission_required = 'info.add_founditem'


class FoundItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # duplicates
    form_class = FoundItemForm
    model = FoundItem
    template_name = 'info/item_form_update.html'
    permission_required = 'info.change_founditem'


class FoundItemDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # duplicates
    model = FoundItem
    success_url = reverse_lazy('info_item_list_found_urlpattern')
    # context_object_name = 'item'
    permission_required = 'info.delete_founditem'


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
            {'site': site, 'item_list': item_list}
        )


class SiteCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SiteForm
    model = Site
    permission_required = 'info.add_site'


class SiteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SiteForm
    model = Site
    template_name = 'info/site_form_update.html'
    permission_required = 'info.change_site'


class SiteDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'info.delete_site'

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


class AdviceList(PageLinksMixin, ListView):
    paginate_by = 15
    model = Advice


class AdviceDetail(View):

    def get(self, request, pk):
        advice = get_object_or_404(
            Advice,
            pk=pk
        )
        return render(
            request,
            'info/advice_detail.html',
            {'advice': advice}
        )


class AdviceCreate(CreateView):
    form_class = AdviceForm
    model = Advice


class AdviceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # duplicates
    model = Advice
    success_url = reverse_lazy('info_advice_list_urlpattern')
    # context_object_name = 'item'
    permission_required = 'info.delete_advice'
