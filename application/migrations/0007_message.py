# Generated by Django 5.1.1 on 2024-12-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_ngocategory_ngogallery_ngo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]