# Generated by Django 2.1.15 on 2020-08-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0006_auto_20200819_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(default='', max_length=20)),
                ('carddesc', models.CharField(default='', max_length=100)),
                ('cardbuy', models.CharField(default='', max_length=10)),
                ('cardImage', models.ImageField(default='', height_field=200, upload_to='E_Commerce/Cards', width_field=100)),
            ],
        ),
    ]
