# Generated by Django 5.0.6 on 2024-09-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="yazar",
            field=models.CharField(
                blank=True, max_length=25, null=True, verbose_name="Yazar İsmi"
            ),
        ),
    ]
