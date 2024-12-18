# Generated by Django 5.0.6 on 2024-10-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_post_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="images",
        ),
        migrations.AddField(
            model_name="post",
            name="descriptionOne",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Ek 1 Açıklama"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="descriptionThree",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Ek 1 Açıklama"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="descriptionTwo",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Ek 1 Açıklama"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="imageOne",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Ek 1"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="imageThree",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Ek 3"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="imageTwo",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Ek 2"
            ),
        ),
    ]
