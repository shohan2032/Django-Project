# Generated by Django 4.0.1 on 2022-02-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_Panel', '0003_owner_panel_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_panel',
            name='Facebook_URL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='owner_panel',
            name='Instagram_URL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='owner_panel',
            name='Linkedin_URL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
