# Generated by Django 5.1.7 on 2025-03-20 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_instagramm', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
    ]
