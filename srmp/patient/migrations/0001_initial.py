# Generated by Django 4.2.4 on 2023-08-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("fullname", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                ("admit", models.BooleanField(default=True)),
                ("commnt", models.TextField()),
                ("image", models.ImageField(upload_to="photos/%d/%m/%y")),
                ("specialitesmedicales", models.TextField()),
                ("Anneesdepratique", models.DateField()),
                ("Certificationsprofessionnelles", models.CharField(max_length=200)),
            ],
        ),
    ]
