# Generated by Django 4.1.2 on 2022-10-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TwitterApp",
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
                ("name", models.CharField(max_length=300)),
                ("tweet", models.TextField()),
                ("dateCreated", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
