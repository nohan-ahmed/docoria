# Generated by Django 5.0.7 on 2024-10-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_code', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
