from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsTeacher, IsStudent
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  

    def get_permissions(self):
        if self.action == 'list':  
            return [IsAdmin()]  
        elif self.action == 'create':  
            return [IsAdmin()]  
        elif self.action == 'update' or self.action == 'partial_update':  
            return [IsAdmin()]  
        return super().get_permissions()
