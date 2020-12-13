from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from .serializers import CategoriaSerializer
from core.models import Artigo
from .serializers import ArtigoSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer


class ArtigoViewSet(ModelViewSet):

    serializer_class = ArtigoSerializer

    def get_queryset(self):
        return Artigo.objects.filter(aprovado=True).order_by('data')
