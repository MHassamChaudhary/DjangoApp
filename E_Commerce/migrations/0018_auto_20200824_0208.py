# Generated by Django 3.1 on 2020-08-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0017_specialoffers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialoffers',
            name='men_prod_image',
            field=models.ImageField(default='', upload_to='E_Commerce/SpecialOffers'),
        ),
    ]
