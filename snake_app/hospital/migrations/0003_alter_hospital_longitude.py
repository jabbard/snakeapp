# Generated by Django 4.2.1 on 2023-06-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0002_alter_hospital_latitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospital", name="longitude", field=models.FloatField(),
        ),
    ]