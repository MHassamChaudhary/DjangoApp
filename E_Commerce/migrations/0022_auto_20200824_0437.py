# Generated by Django 3.1 on 2020-08-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0021_auto_20200824_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffers',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specialoffers',
            name='arrives',
            field=models.CharField(default='', max_length=10),
        ),
    ]
