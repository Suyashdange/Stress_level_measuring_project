# Generated by Django 5.1.3 on 2024-12-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_alter_registration_data_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="appointement_data",
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
                ("appointmentid", models.CharField(max_length=50)),
                ("counsellorid", models.CharField(max_length=50)),
                ("userid", models.DateField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=50)),
                ("date", models.CharField(max_length=50)),
                ("time", models.DateField(max_length=50)),
                ("address", models.DateField(max_length=50)),
                ("result", models.DateField(max_length=50)),
                ("status", models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="StressAssessmentResponse",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("responses", models.JSONField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
