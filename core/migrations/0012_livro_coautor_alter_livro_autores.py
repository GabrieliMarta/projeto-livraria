# Generated by Django 5.1.7 on 2025-04-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_livro_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='coautor',
            field=models.ManyToManyField(blank=True, related_name='livros_coautor', to='core.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='livros_autor', to='core.autor'),
        ),
    ]
