# Generated by Django 5.0.6 on 2024-05-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_event_end_date_alter_event_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='/', upload_to='images'),
        ),
    ]
