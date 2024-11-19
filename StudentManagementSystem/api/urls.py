from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, GradeViewSet, StudentViewSet, AttendanceViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'notifications', NotificationViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
