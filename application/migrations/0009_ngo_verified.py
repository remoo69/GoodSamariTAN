# Generated by Django 5.1.1 on 2024-12-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
