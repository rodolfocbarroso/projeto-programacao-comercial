from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):

    queryset = Avaliacao.objects.all().order_by('data')
    serializer_class = AvaliacaoSerializer
    filter_backends = [SearchFilter]
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

    search_fields = ['=usuario__username']
