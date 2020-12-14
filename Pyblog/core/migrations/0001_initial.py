# Generated by Django 3.1.3 on 2020-11-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, verbose_name='Tema')),
                ('photo', models.URLField(verbose_name='Foto')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'tema',
                'verbose_name_plural': 'temas',
            },
        ),
    ]
