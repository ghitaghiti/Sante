# Generated by Django 4.2 on 2023-09-21 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("radical", "0002_question_answer"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Answer",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
