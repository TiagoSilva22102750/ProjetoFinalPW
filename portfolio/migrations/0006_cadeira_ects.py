# Generated by Django 4.0.4 on 2022-05-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_cadeira_rating_alter_projeto_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='ects',
            field=models.IntegerField(default=1),
        ),
    ]
