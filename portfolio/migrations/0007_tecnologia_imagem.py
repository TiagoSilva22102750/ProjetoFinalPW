# Generated by Django 4.0.4 on 2022-06-17 14:04

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_tfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnologia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=portfolio.models.resolution_path),
        ),
    ]
