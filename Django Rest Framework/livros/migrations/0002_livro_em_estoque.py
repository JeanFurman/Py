# Generated by Django 4.1.7 on 2023-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='em_estoque',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
