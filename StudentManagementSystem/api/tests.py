from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from students.models import Student
from grades.models import Grade
from courses.models import Course
from attendance.models import Attendance

class RoleBasedAccessTests(APITestCase):

    def setUp(self):
        # Создание пользователей
        self.admin_user = User.objects.create_user(username='admin', email='admin@example.com', password='password', role='admin')
        self.teacher_user = User.objects.create_user(username='teacher', email='teacher@example.com', password='password', role='teacher')
        self.student_user = User.objects.create_user(username='student', email='student@example.com', password='password', role='student')

        # Создание объектов
        self.student = Student.objects.create(
            user=self.student_user,
            first_name="Student",
            last_name="One",
            date_of_birth="2000-01-01"
        )
        self.grade = Grade.objects.create(student=self.student, grade=90, course="Math")
        self.course = Course.objects.create(name="Math")
        self.attendance = Attendance.objects.create(student=self.student, course=self.course)

    def test_student_update_own_record(self):
        self.client.login(username='student', password='password')
        url = reverse('student-detail', kwargs={'pk': self.student.id})
        data = {'first_name': 'Updated', 'last_name': 'Student'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_create_grade(self):
        self.client.login(username='teacher', password='password')
        url = reverse('grade-list')
        data = {'student': self.student.id, 'grade': 95, 'course': 'Math'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_access_all_data(self):
        self.client.login(username='admin', password='password')
        url = reverse('grade-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
