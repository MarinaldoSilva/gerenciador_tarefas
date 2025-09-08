from rest_framework import serializers
from .models import Tarefa

class Tarefaerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        #fields = '__all__'
        fields = ['titulo', 'descricao', 'data_criacao', 'concluido', 'dono',  'id']
    #fora dos arquivos de metadados
    dono = serializers.StringRelatedField(read_only=True)
    
    """
    dono -> vai sobreescrever o comportamento padrão do serializer para o campo.
    Serializer por padrão em campos -'fk' retorna seu id e agora com isso, estamos esquecendo o modelo padrão e indo direto para o nosso modelo personalizado

    StringRelatedField -> vai acessar meu Obj User que é um fk em class Tarefa, vai chamar o metodo __str__() que seria o mesmo que toString() em java e por pdrão retorna o username, e ao inves de retornar um interio com o id do user, retorne o username

    read_only -> o campo dono não pode ser reescrito, não pode ser recebido via nenhum metodo, somente verbos GET podem acessar
    """

        #read_only_fields = ['dono'] retorna o id do dono, somente GET