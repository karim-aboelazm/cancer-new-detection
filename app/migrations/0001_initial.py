# Generated by Django 4.2 on 2023-05-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SkinImagePrediction",
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
                ("image", models.ImageField(upload_to="skin/")),
                ("classes", models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                "verbose_name_plural": "Skin Image Prediction",
            },
        ),
    ]
