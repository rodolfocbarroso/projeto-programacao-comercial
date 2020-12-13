from rest_framework.serializers import ModelSerializer
from core.models import Categoria
from core.models import Artigo


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome', 'descricao', 'categoriaPai', 'ativa')


class ArtigoSerializer(ModelSerializer):
    class Meta:
        model = Artigo
        fields = ('id', 'nome', 'descricao', 'imagemUrl',
                  'conteudo', 'data', 'usuario', 'categoria',
                  'comentarios', 'avaliacoes', 'aprovado')