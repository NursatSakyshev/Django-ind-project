from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    # students = models.ManyToManyField('students.Student', related_name='courses')

    def __str__(self):
        return self.name

