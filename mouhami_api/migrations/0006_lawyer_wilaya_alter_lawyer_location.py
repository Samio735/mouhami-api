# Generated by Django 5.0 on 2024-01-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouhami_api', '0005_merge_20240125_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='wilaya',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
