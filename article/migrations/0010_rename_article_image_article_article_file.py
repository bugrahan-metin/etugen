# Generated by Django 5.0.6 on 2024-06-21 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_article_article_image_alter_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_image',
            new_name='article_file',
        ),
    ]