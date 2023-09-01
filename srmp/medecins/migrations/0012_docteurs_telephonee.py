# Generated by Django 4.2.4 on 2023-08-31 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("medecins", "0011_remove_docteurs_telephone"),
    ]

    operations = [
        migrations.AddField(
            model_name="docteurs",
            name="Telephonee",
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
