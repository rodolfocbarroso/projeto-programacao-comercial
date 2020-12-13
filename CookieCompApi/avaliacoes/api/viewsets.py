from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):

    queryset = Avaliacao.objects.all().order_by('data')
    serializer_class = AvaliacaoSerializer
