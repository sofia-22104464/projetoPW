# Generated by Django 4.0.4 on 2022-06-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_tecnologia_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnologia',
            name='tipo',
            field=models.CharField(default='', max_length=31),
        ),
    ]
