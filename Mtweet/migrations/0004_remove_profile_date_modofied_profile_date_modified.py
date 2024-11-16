# Generated by Django 5.1.2 on 2024-11-08 01:51

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Mtweet", "0003_alter_profile_date_modofied"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="date_modofied",
        ),
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]