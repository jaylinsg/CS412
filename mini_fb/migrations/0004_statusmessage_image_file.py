# Generated by Django 5.2.1 on 2025-06-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_remove_profile_profile_image_url_profile_image_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
