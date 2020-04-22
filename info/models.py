from django.db import models
from django.urls import reverse
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Site(models.Model):
    site_id = models.AutoField(primary_key = True)
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


class User(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, null=False)
    phone = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return '%s %s'%(self.first_name, self.last_name)


class Item(models.Model):
    item_id = models.AutoField(primary_key = True)
    item_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=(('L', 'Lost'), ('F', "Found"),)) # lost or found
    place = models.CharField(max_length=80) # where the item is found or lost
    eventDate = models.DateField()
    eventTime = models.CharField(max_length=20) # like 'around 2pm'
    registeredTime = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
    ps = models.CharField(max_length=80, null=True, blank=True)

    site = models.ForeignKey(Site, related_name='items', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='items', on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s at %s' % (self.item_name, self.type, self.place)

    class Meta:
        ordering = ['registeredTime']

    def get_absolute_url(self):
        return reverse('info_item_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('info_item_update_urlpattern',
                       kwargs={'pk': self.pk})