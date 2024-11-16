# Generated by Django 5.1.2 on 2024-11-08 00:43

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Mtweet", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modofied",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="follows",
            field=models.ManyToManyField(
                blank=True, related_name="followed_by", to="Mtweet.profile"
            ),
        ),
    ]