# Generated by Django 4.2 on 2023-09-25 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_users"),
    ]

    operations = [
        migrations.RenameField(
            model_name="users",
            old_name="code_answer",
            new_name="Recommander",
        ),
        migrations.RenameField(
            model_name="users",
            old_name="question",
            new_name="symptoms",
        ),
        migrations.RenameField(
            model_name="users",
            old_name="language",
            new_name="villes",
        ),
    ]