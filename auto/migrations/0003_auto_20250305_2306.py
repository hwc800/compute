# Generated by Django 3.2.25 on 2025-03-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_requesttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='compute_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='compute_count',
            field=models.IntegerField(default=0),
        ),
    ]
