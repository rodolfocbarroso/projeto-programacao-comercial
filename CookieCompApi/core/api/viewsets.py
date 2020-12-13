from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from .serializers import CategoriaSerializer
from core.models import Artigo
from .serializers import ArtigoSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer


class ArtigoViewSet(ModelViewSet):

    queryset = Artigo.objects.all().order_by('data')
    serializer_class = ArtigoSerializer
