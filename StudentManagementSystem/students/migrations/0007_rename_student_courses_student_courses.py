# Generated by Django 5.1.3 on 2024-11-19 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0006_student_student_courses"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="student_courses",
            new_name="courses",
        ),
    ]
