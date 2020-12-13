from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from .serializers import CategoriaSerializer
from core.models import Artigo
from .serializers import ArtigoSerializer


class CategoriaViewSet(ModelViewSet):

    serializer_class = CategoriaSerializer

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        queryset = Categoria.objects.filter(ativa=True)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset.order_by('nome')


class ArtigoViewSet(ModelViewSet):

    serializer_class = ArtigoSerializer
    filterset_fields = ['categoria', 'usuario']
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']

    def get_queryset(self):
        return Artigo.objects.filter(aprovado=True).order_by('data')

