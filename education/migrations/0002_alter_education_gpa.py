# Generated by Django 5.0.7 on 2024-10-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
