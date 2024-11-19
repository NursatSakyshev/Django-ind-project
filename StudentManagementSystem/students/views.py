# students/views.py
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from courses.models import Course

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Действие для записи студента на курс
    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        student = self.get_object()
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found'}, status=404)

        student.courses.add(course)
        return Response({'detail': 'Enrolled successfully'}, status=200)

    # Действие для удаления курса из списка курсов студента
    @action(detail=True, methods=['post'])
    def unenroll(self, request, pk=None):
        student = self.get_object()
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found'}, status=404)

        student.courses.remove(course)
        return Response({'detail': 'Unenrolled successfully'}, status=200)
