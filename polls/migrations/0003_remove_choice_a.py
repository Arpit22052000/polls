# Generated by Django 5.0 on 2023-12-27 16:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_choice_a_alter_choice_votes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="choice",
            name="a",
        ),
    ]