# Generated by Django 5.1.3 on 2024-12-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_alter_test_data_date_alter_test_data_result_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test_data",
            name="username",
            field=models.EmailField(max_length=255),
        ),
    ]
