from rest_framework.serializers import ModelSerializer
from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome', 'descricao', 'categoriaPai')