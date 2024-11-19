from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from api.permissions import IsStudent, IsTeacher
from attendance.models import Attendance
from notifications.models import Notification
from students.models import Student
from courses.models import Course
from grades.models import Grade
from .serializers import AttendanceSerializer, CourseSerializer, GradeSerializer, NotificationSerializer, StudentSerializer
from api.permissions import IsStudent, IsTeacher, IsAdmin

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdmin()]  
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  
        if self.action in ['update', 'partial_update']:
            return [IsStudent()]  
        return [IsAdmin()]  

    def get_queryset(self):
        if self.action == 'list':
            return Student.objects.filter(user=self.request.user)  
        return super().get_queryset()


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsTeacher()]  
        return [IsAdmin()]

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsTeacher()] 
        return [IsAdmin()]  

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsTeacher()]
        return [IsAdmin()]  


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer