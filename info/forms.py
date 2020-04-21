from django import forms

from info.models import Site, Item


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

    def clean_site_name(self):
        return self.cleaned_data['site_name'].strip()

    def clean_location(self):
        return self.cleaned_data['location'].strip()

    def clean_contact(self):
        return self.cleaned_data['contact']



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def clean_item_name(self):
        return self.cleaned_data['item_name'].strip()

    def clean_place(self):
        return self.cleaned_data['place'].strip()

    def clean_eventTime(self):
        return self.cleaned_data['eventTime'].strip()

    def clean_ps(self):
        if self.cleaned_data['ps']:
            return self.cleaned_data['ps'].strip()