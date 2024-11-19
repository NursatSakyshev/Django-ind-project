from django.contrib import admin
from .models import Student

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrolled_date', 'courses')  
    list_filter = ('enrolled_date',)  
    search_fields = ('first_name', 'last_name')  

    def courses(self, obj):
        return ", ".join([course.name for course in obj.courses.all()])  
    
    courses.short_description = 'courses'