# Generated by Django 4.1.7 on 2023-03-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='nome',
            field=models.TextField(max_length=23),
        ),
    ]
