# Generated by Django 4.0.4 on 2022-05-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_laboratorio_link_alter_laboratorio_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('linkNoticia', models.URLField(blank=True, default='', null=True)),
            ],
        ),
    ]
