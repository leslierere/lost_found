# Generated by Django 3.0.3 on 2020-04-29 20:04

from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

SITES = [
    {'site_name': 'Test0 Library', 'location': 'Test0 St', 'contact': 1000000},
    {'site_name': 'Test1 Library', 'location': 'Test1 St', 'contact': 1000001},
    {'site_name': 'Test2 Library', 'location': 'Test2 St', 'contact': 1000002},
    {'site_name': 'Test3 Library', 'location': 'Test3 St', 'contact': 1000003},
    {'site_name': 'Test4 Library', 'location': 'Test4 St', 'contact': 1000004},
    {'site_name': 'Test5 Library', 'location': 'Test5 St', 'contact': 1000005},
    {'site_name': 'Test6 Library', 'location': 'Test6 St', 'contact': 1000006},
    {'site_name': 'Test7 Library', 'location': 'Test7 St', 'contact': 1000007},
    {'site_name': 'Test8 Library', 'location': 'Test8 St', 'contact': 1000008},
    {'site_name': 'Test9 Library', 'location': 'Test9 St', 'contact': 1000009},
    {'site_name': 'Test10 Library', 'location': 'Test10 St', 'contact': 1000010},
    {'site_name': 'Test11 Library', 'location': 'Test11 St', 'contact': 1000011},
    {'site_name': 'Test12 Library', 'location': 'Test12 St', 'contact': 1000012},
    {'site_name': 'Test13 Library', 'location': 'Test13 St', 'contact': 1000013},
    {'site_name': 'Test14 Library', 'location': 'Test14 St', 'contact': 1000014},
    {'site_name': 'Test15 Library', 'location': 'Test15 St', 'contact': 1000015},
    {'site_name': 'Test16 Library', 'location': 'Test16 St', 'contact': 1000016},
    {'site_name': 'Test17 Library', 'location': 'Test17 St', 'contact': 1000017},
    {'site_name': 'Test18 Library', 'location': 'Test18 St', 'contact': 1000018},
    {'site_name': 'Test19 Library', 'location': 'Test19 St', 'contact': 1000019},
    {'site_name': 'Test20 Library', 'location': 'Test20 St', 'contact': 1000020},
    {'site_name': 'Test21 Library', 'location': 'Test21 St', 'contact': 1000021},
    {'site_name': 'Test22 Library', 'location': 'Test22 St', 'contact': 1000022},
    {'site_name': 'Test23 Library', 'location': 'Test23 St', 'contact': 1000023},
    {'site_name': 'Test24 Library', 'location': 'Test24 St', 'contact': 1000024},
    {'site_name': 'Test25 Library', 'location': 'Test25 St', 'contact': 1000025},
    {'site_name': 'Test26 Library', 'location': 'Test26 St', 'contact': 1000026},
    {'site_name': 'Test27 Library', 'location': 'Test27 St', 'contact': 1000027},
    {'site_name': 'Test28 Library', 'location': 'Test28 St', 'contact': 1000028},
    {'site_name': 'Test29 Library', 'location': 'Test29 St', 'contact': 1000029},
]


def add_site_data(apps, schema_editor):
    site_class = apps.get_model('info', 'Site')
    for site in SITES:
        try:
            duplicate_object = site_class.objects.get(
                site_name=site['site_name'],
                location=site['location'],
                contact=site['contact'],
            )
            print('Duplicate instructor entry not added to instructor table:', site['site_name'],
                  site['location'])
        except ObjectDoesNotExist:
            site_object = site_class.objects.create(
                site_name=site['site_name'],
                location=site['location'],
                contact = site['contact']
            )


def remove_site_data(apps, schema_editor):
    site_class = apps.get_model('info', 'Site')
    for site in SITES:
        site_object = site_class.objects.get(
            site_name=site['site_name'],
            location=site['location'],
            contact=site['contact']
        )
        site_object.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('info', '0012_auto_20200424_1639'),
    ]

    operations = [
        migrations.RunPython(
            add_site_data,
            remove_site_data
        )
    ]