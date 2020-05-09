from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=45, unique=True)
    location = models.CharField(max_length=80, unique=True)
    contact = models.IntegerField()

    def __str__(self):
        return '%s' % self.site_name

    def get_absolute_url(self):
        return reverse('info_site_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('info_site_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('info_site_delete_urlpattern',
                       kwargs={'pk': self.pk})


# class User(models.Model):
#     id = models.AutoField(primary_key = True)
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     email = models.EmailField(max_length=254, null=False)
#     phone = PhoneNumberField(null=True, blank=True)
#
#     def __str__(self):
#         return '%s %s'%(self.first_name, self.last_name)


class LostItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=30)
    place = models.CharField(max_length=80)  # where the item is lost
    eventDate = models.DateField()
    eventTime = models.CharField(max_length=20)  # like 'around 2pm'
    registeredTime = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField()
    description = models.CharField(max_length=80, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)  # may changed to be autofilled later
    email = models.EmailField()
    found = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s lost at %s' % (self.item_name, self.place)

    class Meta:
        ordering = ['registeredTime']

    def get_absolute_url(self):
        return reverse('info_lostitem_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('info_item_update_lost_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('info_item_delete_lost_urlpattern',
                       kwargs={'pk': self.pk})


class FoundItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=30)
    place = models.CharField(max_length=80)  # where the item is found or lost
    eventDate = models.DateField()
    eventTime = models.CharField(max_length=20)  # like 'around 2pm'
    registeredTime = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField()
    description = models.CharField(max_length=80, null=True, blank=True)
    # userContact = PhoneNumberField(null=True, blank=True)

    picked = models.BooleanField(default=False)
    pickedBy = models.CharField(max_length=50, blank=True, default='')
    phone = PhoneNumberField(null=True, blank=True)  # may changed to be autofilled later
    email = models.EmailField(blank=True)
    pickedTime = models.DateTimeField(blank=True, null=True)
    pickedInfo = models.CharField(max_length=80, blank=True, default='')
    admin = models.CharField(max_length=30, blank=True, default='')  # the administrator who process the pickedUp

    site = models.ForeignKey(Site, related_name='items', on_delete=models.PROTECT)

    def __str__(self):
        return '%s found at %s' % (self.item_name, self.place)

    class Meta:
        ordering = ['registeredTime']

    def get_absolute_url(self):
        return reverse('info_founditem_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('info_item_update_found_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('info_item_delete_found_urlpattern',
                       kwargs={'pk': self.pk})


class Advice(models.Model):
    advice_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    email = models.EmailField()
    given_time = models.DateTimeField(auto_now_add=True)
    site = models.ForeignKey(Site, related_name='advices', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Advice at %s' % (self.given_time.strftime('%a, %b %d, %y %H:%M'))

    class Meta:
        ordering = ['given_time']

    def get_absolute_url(self):
        return reverse('info_advice_detail_urlpattern',
                       kwargs={'pk': self.pk})

    #
    # def get_update_url(self):
    #     return reverse('info_item_update_found_urlpattern',
    #                    kwargs={'pk': self.pk})
    #
    def get_delete_url(self):
        return reverse('info_advice_delete_urlpattern',
                       kwargs={'pk': self.pk})
