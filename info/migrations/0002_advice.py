# Generated by Django 3.0.3 on 2020-05-08 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('advice_id', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('given_time', models.DateTimeField(auto_now_add=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advices', to='info.Site')),
            ],
            options={
                'ordering': ['given_time'],
            },
        ),
    ]
