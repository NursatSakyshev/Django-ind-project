from django.db import models

class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)  

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade}"

