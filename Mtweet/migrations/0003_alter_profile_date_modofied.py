# Generated by Django 5.1.2 on 2024-11-08 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Mtweet", "0002_profile_date_modofied_alter_profile_follows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="date_modofied",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
