from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# from api.permissions import IsStudent, IsTeacher
from attendance.models import Attendance
from notifications.models import Notification
from students.models import Student
from courses.models import Course
from grades.models import Grade
from .serializers import AttendanceSerializer, CourseSerializer, GradeSerializer, NotificationSerializer, StudentSerializer
from api.permissions import IsStudent, IsTeacher

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.action == 'list':
            return Student.objects.filter(user=self.request.user)  
        return super().get_queryset()


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def create(self, request, *args, **kwargs):
        # Custom logic before saving
        data = request.data
        user = request.user
        print("create")
        if user.role != "teacher":
            return Response('Permission denied', status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        user = request.user
        print("update")
        if user.role != "teacher":
            return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        print("create")
        if user.role != "teacher":
            return Response('Permission denied', status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        user = request.user
        print("update")
        if user.role != "teacher":
            return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)



class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
