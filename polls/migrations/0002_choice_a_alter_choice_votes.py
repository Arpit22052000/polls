# Generated by Django 5.0 on 2023-12-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="a",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="choice",
            name="votes",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
