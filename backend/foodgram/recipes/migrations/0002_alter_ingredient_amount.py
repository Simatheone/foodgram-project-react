# Generated by Django 4.0.4 on 2022-04-26 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Количество'),
        ),
    ]
