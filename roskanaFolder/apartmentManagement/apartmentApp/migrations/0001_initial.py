# Generated by Django 3.2.18 on 2024-04-30 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('property_type', models.CharField(max_length=200)),
                ('property_numRooms', models.PositiveIntegerField()),
                ('property_numPeopleCurrent', models.PositiveIntegerField()),
                ('property_image', models.ImageField(upload_to='property/')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_email', models.EmailField(max_length=254)),
                ('owner_phone', models.CharField(max_length=20)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('number_of_reviews', models.PositiveIntegerField(default=0)),
                ('facilities', models.ManyToManyField(to='apartmentApp.Facility')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=50)),
                ('room_type', models.CharField(max_length=100)),
                ('occupancy', models.PositiveIntegerField()),
                ('bed_type', models.CharField(max_length=100)),
                ('rent_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='apartmentApp.property')),
            ],
        ),
    ]
