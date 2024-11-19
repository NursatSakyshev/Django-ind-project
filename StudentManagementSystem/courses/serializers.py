from rest_framework import serializers
from .models import Course
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)  

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'start_date', 'end_date' 'instructor')
        