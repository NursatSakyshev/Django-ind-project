from celery import shared_task
from django.shortcuts import get_object_or_404
from .models import Student
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_student_notification(student_id, message):
    student = get_object_or_404(Student, id=student_id)
    
    logger.info(f"Sending notification to {student}: {message}")
    
    return f"Notification sent to {student.first_name} {student.last_name}"
