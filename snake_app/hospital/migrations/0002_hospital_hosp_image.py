# Generated by Django 4.2.1 on 2023-05-20 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hospital",
            name="hosp_image",
            field=models.ImageField(blank=True, null=True, upload_to="hospital/"),
        ),
    ]