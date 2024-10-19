# Generated by Django 5.1.2 on 2024-10-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('last_name', models.CharField(blank=True, max_length=246, null=True)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'Customer'), (2, 'Business')], null=True)),
                ('phone_number', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('pincode', models.CharField(blank=True, max_length=120, null=True)),
                ('is_super', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
