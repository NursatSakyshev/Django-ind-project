# Generated by Django 5.1.3 on 2024-11-21 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"role": "teacher"},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses_taught",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]