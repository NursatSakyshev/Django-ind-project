from rest_framework import serializers
from .models import Student
from courses.serializers import CourseSerializer

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'enrolled_date', 'courses')