from rest_framework.viewsets import ModelViewSet
from attendance.models import Attendance
from notifications.models import Notification
from students.models import Student
from courses.models import Course
from grades.models import Grade
from .serializers import AttendanceSerializer, CourseSerializer, GradeSerializer, NotificationSerializer, StudentSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer