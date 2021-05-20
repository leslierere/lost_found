import datetime

from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=45, unique=True)
    location = models.CharField(max_length=80, unique=True)
    contact = PhoneNumberField()

    def __str__(self):
        return '%s' % self.site_name

    def get_absolute_url(self):
        return reverse('info_site_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('info_site_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_map_url(self):
        if self.site_name=="Main library":
            return "https://goo.gl/maps/nBsAbiuw7Yf4bcoi9"
        elif self.site_name=="Grainger":
            return "https://goo.gl/maps/4r5uQGRwXP7sXdicA"
        elif self.site_name=="Undergrad Library":
            return "https://goo.gl/maps/uvpx6GuJmeZ34173A"
        elif self.site_name=="FUNK":
            return "https://goo.gl/maps/yEj7qVGoczt9S4xt7"

    def get_real_map_url(self):
        if self.site_name=="Main library":
            return "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3051.686215138374!2d-88.23119908522251!3d40.104708482481705!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd73db42cf56b%3A0xea81d21581484965!2sMain%20Library!5e0!3m2!1sen!2sus!4v1621482153908!5m2!1sen!2sus"
        elif self.site_name=="Grainger":
            return "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3051.33650358391!2d-88.22910588522228!3d40.11250378201058!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd76a968358b5%3A0xae7c7d5e32439ec2!2sGrainger%20Engineering%20Library!5e0!3m2!1sen!2sus!4v1621482123561!5m2!1sen!2sus"
        elif self.site_name=="Undergrad Library":
            return "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3051.686071592053!2d-88.22909918522257!3d40.104711682481515!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd73d8d6ccc6d%3A0x8660329536de34ae!2sUndergraduate%20Library!5e0!3m2!1sen!2sus!4v1621482096544!5m2!1sen!2sus"
        elif self.site_name=="FUNK":
            return "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3051.7707577815722!2d-88.22729948522262!3d40.1028237825957!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd717b0f51ec1%3A0x5ec7f43f8cadd9bf!2sFunk%20Agricultural%2C%20Consumer%2C%20and%20Environmental%20Sciences%20Library%20(Funk%20ACES)!5e0!3m2!1sen!2sus!4v1621481901850!5m2!1sen!2sus"

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
    eventDate = models.DateField(default=datetime.date.today)
    eventTime = models.CharField(max_length=20)  # like 'around 2pm'
    registeredTime = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField()
    description = models.CharField(max_length=80, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)  # may changed to be autofilled later
    email = models.EmailField()
    found = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lost_item_img', blank=True)

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
    eventDate = models.DateField(default=datetime.date.today)
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
    image = models.ImageField(upload_to='found_item_img', blank=True)

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
