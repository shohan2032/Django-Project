# Generated by Django 4.0.1 on 2022-02-03 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ownerlogin', '0002_rename_coders_owner_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='owner_login',
        ),
    ]
