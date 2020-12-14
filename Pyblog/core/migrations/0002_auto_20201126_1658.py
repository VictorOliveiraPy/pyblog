# Generated by Django 3.1.3 on 2020-11-26 19:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name': 'Título', 'verbose_name_plural': 'Títulos'},
        ),
        migrations.RemoveField(
            model_name='publish',
            name='description',
        ),
        migrations.RemoveField(
            model_name='publish',
            name='theme',
        ),
        migrations.AddField(
            model_name='publish',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1, verbose_name='Conteudo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publish',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publish',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Título'),
            preserve_default=False,
        ),
    ]