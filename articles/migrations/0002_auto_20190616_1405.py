# Generated by Django 2.1.1 on 2019-06-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='Телефон'),
        ),
    ]
