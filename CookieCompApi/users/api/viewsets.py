from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group
from .serializers import UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = UserSerializer

