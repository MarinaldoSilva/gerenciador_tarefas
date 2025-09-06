from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import Tarefaerializer
from .models import Tarefa

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = Tarefaerializer
    permission_classes = [permissions.IsAuthenticated]#obrigatórtio ser autenticado
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['concluido']
    
    def get_queryset(self):
        return Tarefa.objects.filter(dono = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono = self.request.user)

