# Generated by Django 4.2 on 2025-06-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_heroimagemobile_heroimageswiperone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]
