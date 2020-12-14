from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):

    queryset = Comentario.objects.all().order_by('data')
    serializer_class = ComentarioSerializer
    filter_backends = [SearchFilter]
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

    search_fields = ['=usuario__username']
