# Generated by Django 4.2.11 on 2024-03-12 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='game_images'),
        ),
        migrations.AddField(
            model_name='game',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='publisher',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
