# Generated by Django 3.1 on 2020-08-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0019_auto_20200824_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffers',
            name='arrives',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='specialoffers',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
