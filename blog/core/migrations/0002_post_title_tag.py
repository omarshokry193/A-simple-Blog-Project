# Generated by Django 4.0.4 on 2022-06-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]