# Generated by Django 4.0.4 on 2022-06-12 13:40

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_aptidoesecompetencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='escola',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=portfolio.models.resolution_path),
        ),
    ]
