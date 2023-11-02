# Generated by Django 4.2.6 on 2023-10-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuditoriumEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=255)),
                ("event_description", models.TextField()),
                ("expected_attendees", models.IntegerField()),
                ("booking_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="SeatBooking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat_row", models.IntegerField()),
                ("seat_column", models.IntegerField()),
                ("attendee_name", models.CharField(max_length=255)),
                ("contact_info", models.CharField(max_length=255)),
                ("is_booked", models.BooleanField(default=False)),
            ],
        ),
    ]
