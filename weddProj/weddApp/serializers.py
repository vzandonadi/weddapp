from django.contrib.auth.models import User, Group
from weddApp.models import Guests, Groups, GroupMsg, IndividualMsg, Confirmed, AppVersion, PushToken
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'

class GuestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class GroupMsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupMsg
        fields = '__all__'

class IndividualMsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndividualMsg
        fields = '__all__'

class ConfirmedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Confirmed
        fields = '__all__'

class AppVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppVersion
        fields = '__all__'

class PushTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PushToken
        fields = '__all__'