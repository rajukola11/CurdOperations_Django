# Generated by Django 5.0.8 on 2024-09-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]