# Generated by Django 3.2.18 on 2024-05-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartmentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(default='', upload_to='rooms/'),
            preserve_default=False,
        ),
    ]