# Generated by Django 4.0.1 on 2022-02-02 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_Panel', '0007_owner_panel_ownership'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_panel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
