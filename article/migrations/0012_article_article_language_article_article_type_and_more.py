# Generated by Django 5.0.6 on 2024-06-21 15:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_article_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_language',
            field=models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('DE', 'German'), ('TR', 'Turkish')], default='TR', max_length=2),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Makale Türü'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Anahtar Kelimeler'),
        ),
        migrations.AddField(
            model_name='article',
            name='publisher_detail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Yazar Detayları'),
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Kaynakça'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Özet'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Yazar İsmi'),
        ),
    ]
