# Generated by Django 3.1 on 2020-08-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0013_auto_20200822_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusSignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserFirstName', models.CharField(default='', max_length=100)),
                ('UserLastName', models.CharField(default='', max_length=100)),
                ('usermail', models.CharField(default='', max_length=100)),
                ('userpass', models.CharField(default='', max_length=300)),
            ],
        ),
    ]