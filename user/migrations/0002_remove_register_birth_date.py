# Generated by Django 5.0.6 on 2024-09-10 14:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="register",
            name="birth_date",
        ),
    ]