from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):

    queryset = Comentario.objects.all().order_by('data')
    serializer_class = ComentarioSerializer
