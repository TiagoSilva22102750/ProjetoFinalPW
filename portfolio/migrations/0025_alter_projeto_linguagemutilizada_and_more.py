# Generated by Django 4.0.4 on 2022-05-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_alter_cadeira_linguagens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='linguagemUtilizada',
            field=models.ManyToManyField(related_name='linguagemUsada', to='portfolio.linguagen'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='participantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='participantes', to='portfolio.pessoa'),
        ),
    ]
