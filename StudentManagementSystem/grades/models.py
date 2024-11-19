from django.db import models
import django.utils
from datetime import date
from users.models import User

class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)  
    # date = models.DateField()  
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='grades_given', limit_choices_to={'role': 'teacher'})  

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade}"

