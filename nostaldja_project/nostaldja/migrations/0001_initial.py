# Generated by Django 4.1.7 on 2023-03-29 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Decades",
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
                ("start_year", models.DateField()),
                ("end_year", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Fads",
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
                ("name", models.CharField(max_length=255)),
                ("image_url", models.TextField()),
                ("description", models.TextField()),
                (
                    "decade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fad",
                        to="nostaldja.decades",
                    ),
                ),
            ],
        ),
    ]
