# Generated by Django 5.1.3 on 2024-11-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_course_students"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="students",
        ),
    ]
