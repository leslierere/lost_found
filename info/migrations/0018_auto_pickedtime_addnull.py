# Generated by Django 3.0.3 on 2020-05-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_auto_set_pickedemail_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditem',
            name='pickedTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]