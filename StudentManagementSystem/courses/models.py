from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='courses_taught', limit_choices_to={'role': 'teacher'})
    
    def __str__(self):
        return self.name

