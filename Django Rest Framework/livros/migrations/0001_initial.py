# Generated by Django 4.1.7 on 2023-03-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]