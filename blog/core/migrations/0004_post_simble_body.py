# Generated by Django 4.0.4 on 2022-06-03 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_post_date_alter_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='simble_body',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
