# Generated by Django 5.1.3 on 2024-11-21 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("attendance", "0001_initial"),
        ("courses", "0001_initial"),
        ("students", "__first__"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.course"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.student"
            ),
        ),
    ]