# Generated by Django 4.0.4 on 2022-05-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_interesse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='docente_praticas',
            field=models.ManyToManyField(related_name='cadeiras', to='portfolio.pessoa'),
        ),
    ]
