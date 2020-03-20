# Generated by Django 3.0.3 on 2020-03-20 17:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=45, unique=True)),
                ('location', models.CharField(max_length=80, unique=True)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=80)),
                ('eventDate', models.DateField()),
                ('eventTime', models.CharField(max_length=20)),
                ('registeredTime', models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 57, 32, 744858, tzinfo=utc))),
                ('quantity', models.IntegerField()),
                ('ps', models.CharField(max_length=80)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='info.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='info.User')),
            ],
        ),
    ]