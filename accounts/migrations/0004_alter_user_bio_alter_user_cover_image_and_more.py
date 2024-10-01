# Generated by Django 5.0.7 on 2024-10-01 20:27

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_cover_image_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.user_directory_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Othsers')], max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.user_directory_path),
        ),
    ]
