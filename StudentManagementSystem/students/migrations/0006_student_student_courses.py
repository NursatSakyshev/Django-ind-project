# Generated by Django 5.1.3 on 2024-11-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_course_students"),
        ("students", "0005_remove_student_courses"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="student_courses",
            field=models.ManyToManyField(
                blank=True, related_name="students_enrolled", to="courses.course"
            ),
        ),
    ]
