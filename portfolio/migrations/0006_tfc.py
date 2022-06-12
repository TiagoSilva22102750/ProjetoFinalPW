# Generated by Django 4.0.4 on 2022-06-12 17:23

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_escola_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TFC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores', models.CharField(max_length=150)),
                ('orientadores', models.CharField(max_length=150)),
                ('ano', models.CharField(max_length=4)),
                ('titulo', models.CharField(max_length=75)),
                ('resumo', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=portfolio.models.resolution_path)),
                ('urlRelatorio', models.URLField(blank=True, default='', null=True)),
                ('urlGitHub', models.URLField(blank=True, default='', null=True)),
                ('urlYouTube', models.URLField(blank=True, default='', null=True)),
            ],
        ),
    ]
