# Generated by Django 5.0.3 on 2024-03-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
    ]
