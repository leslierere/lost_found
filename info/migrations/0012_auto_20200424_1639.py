# Generated by Django 3.0.3 on 2020-04-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='registeredTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]