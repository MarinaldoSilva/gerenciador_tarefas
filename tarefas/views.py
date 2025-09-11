from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import Tarefaerializer
from .models import Tarefa

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = Tarefaerializer
    permission_classes = [permissions.IsAuthenticated]#obrigatórtio ser autenticado
    filter_backends = [
        DjangoFilterBackend, #para filtros exatos
        filters.SearchFilter, #palavras chaves
        filters.OrderingFilter #ordenação personalizada
    ]
    search_fields = ['titulo', 'descricao']
    """pesquisar palavras chaves nos campos acima"""

    ordering_fields = ['titulo', 'data_criacao']
    """ordenar por titulo e pelas data que foram criados"""

    filterset_fields = ['concluido'] 
    """filtro para o campo especifico-> /api/tarefas/?concluido=true/False 
        ver todas as tarefas sem filtrar /api/tarefas/
    """
    
    def get_queryset(self):
        return Tarefa.objects.filter(dono = self.request.user)
    """user só manipula suas próprias tarefas"""
    
    def perform_create(self, serializer):
        serializer.save(dono = self.request.user)
        """vincula o usuário a suas tarefas criadas"""

