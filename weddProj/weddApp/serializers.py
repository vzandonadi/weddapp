from django.contrib.auth.models import User, Group
from weddApp.models import Guests
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GuestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'