# Generated by Django 5.1.2 on 2024-10-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='womendreses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='women_dress/'),
        ),
    ]