# Generated by Django 4.1.7 on 2023-03-16 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_categoria_remove_livro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livros.categoria'),
        ),
    ]
