from rest_framework import permissions
from rest_framework.permissions import BasePermission
# class IsStudent(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'student'

#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user


# class IsTeacher(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'teacher'

#     def has_object_permission(self, request, view, obj):
#         return True


# class IsAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'admin'

#     def has_object_permission(self, request, view, obj):
#         return True

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'