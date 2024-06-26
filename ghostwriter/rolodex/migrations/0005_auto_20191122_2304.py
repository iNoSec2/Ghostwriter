# Generated by Django 2.2.3 on 2019-11-22 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rolodex", "0004_auto_20190910_0113"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="client",
            field=models.ForeignKey(
                help_text="Select the client this project should be attached to",
                on_delete=django.db.models.deletion.CASCADE,
                to="rolodex.Client",
            ),
        ),
    ]
