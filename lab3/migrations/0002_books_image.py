# Generated by Django 4.1.1 on 2023-01-31 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
