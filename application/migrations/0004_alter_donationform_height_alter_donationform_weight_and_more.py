# Generated by Django 5.1.1 on 2024-12-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_remove_donationform_image_url_donationform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationform',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationform',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donationform',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
