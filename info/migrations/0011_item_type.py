# Generated by Django 3.0.3 on 2020-03-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_remove_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('L', 'Lost'), ('F', 'Found')], default='Lost', max_length=10),
            preserve_default=False,
        ),
    ]
