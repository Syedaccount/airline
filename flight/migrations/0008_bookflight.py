# Generated by Django 4.2.1 on 2023-05-20 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_remove_passenger_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='flight.flight')),
                ('passenger', models.ManyToManyField(to='flight.passenger')),
            ],
        ),
    ]
