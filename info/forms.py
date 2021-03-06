import datetime

from django import forms

from info.models import Site, LostItem, FoundItem, Advice


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


class DateInput(forms.DateInput):  # for date selection box
    input_type = 'date'


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        widgets = {'eventDate': DateInput()}
        exclude = ('user',)
        # fields = '__all__'

    def clean_eventDate(self):
        date = self.cleaned_data['eventDate']
        if date > datetime.date.today():
            raise forms.ValidationError("The date cannot be in the future")
        return date

    def clean_item_name(self):
        return self.cleaned_data['item_name'].strip()

    def clean_place(self):
        return self.cleaned_data['place'].strip()

    def clean_eventTime(self):
        return self.cleaned_data['eventTime'].strip()

    def clean_description(self):
        if self.cleaned_data['description']:
            return self.cleaned_data['description'].strip()


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        widgets = {'eventDate': DateInput(), 'pickedTime': DateInput()}
        fields = '__all__'

    def clean_eventDate(self):
        date = self.cleaned_data['eventDate']
        if date > datetime.date.today():
            raise forms.ValidationError("The date cannot be in the future")
        return date

    def clean_item_name(self):
        return self.cleaned_data['item_name'].strip()

    def clean_place(self):
        return self.cleaned_data['place'].strip()

    def clean_eventTime(self):
        return self.cleaned_data['eventTime'].strip()

    def clean_description(self):
        if self.cleaned_data['description']:
            return self.cleaned_data['description'].strip()

    def clean_pickedInfo(self):
        return self.cleaned_data['pickedInfo'].strip()

    def clean_admin(self):
        return self.cleaned_data['admin'].strip()


class AdviceForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = '__all__'

    def clean_contents(self):
        return self.cleaned_data['contents'].strip()
