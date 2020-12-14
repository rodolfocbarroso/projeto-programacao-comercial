from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User, Group


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'groups')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
