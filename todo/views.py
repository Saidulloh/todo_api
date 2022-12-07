from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.serializers import TodoSerializer
from todo.models import Todo
from user.models import User


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user__id=self.request.user.id)
        