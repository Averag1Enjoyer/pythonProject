# Generated by Django 3.2.8 on 2021-11-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Someshit', max_length=50, verbose_name='Назва')),
                ('anons', models.CharField(default='Someshit', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Стаття')),
                ('date', models.DateTimeField(verbose_name='Дата Публікації')),
            ],
        ),
    ]
