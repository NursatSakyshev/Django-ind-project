from django.db import models
from django.conf import settings
from courses.models import Course

class Student(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    enrolled_date = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(Course, related_name='students_enrolled', blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
