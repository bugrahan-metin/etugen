# Generated by Django 5.0.6 on 2024-06-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_article_article_language_article_article_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_language',
            field=models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('DE', 'German'), ('TR', 'Turkish')], default='TR', max_length=2, verbose_name='Makale Dili'),
        ),
    ]
