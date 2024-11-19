from rest_framework.viewsets import ModelViewSet
from students.models import Student
from courses.models import Course
from .serializers import CourseSerializer, StudentSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer