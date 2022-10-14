from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from weddApp.models import Guests, Groups, GroupMsg, IndividualMsg, Confirmed, AppVersion, PushToken
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weddApp.serializers import UserSerializer, GroupSerializer, GuestsSerializer, GroupsSerializer, GroupMsgSerializer, IndividualMsgSerializer, ConfirmedSerializer, AppVersionSerializer, PushTokenSerializer
# Create your views here.

def index(request):
    my_dict = { 'insert_me':"hello i'm from views.py!"}
    return render(request, 'weddApp/index.html', context=my_dict)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permissions_classes = [permissions.IsAuthenticated]

class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    permisson_classes = [permissions.IsAuthenticated]

class GroupMsgViewSet(viewsets.ModelViewSet):
    queryset = GroupMsg.objects.all()
    serializer_class = GroupMsgSerializer
    permissions_classes = [permissions.IsAuthenticated]

class IndividualMsgViewSet(viewsets.ModelViewSet):
    queryset = IndividualMsg.objects.all()
    serializer_class = IndividualMsgSerializer
    permissions_classes = [permissions.IsAuthenticated]

class ConfirmedMsgViewSet(viewsets.ModelViewSet):
    queryset = Confirmed.objects.all()
    serializer_class = ConfirmedSerializer
    permissions_classes = [permissions.IsAuthenticated]

class AppVersionViewSet(viewsets.ModelViewSet):
    queryset = AppVersion.objects.all()
    serializer_class = AppVersionSerializer
    permissions_classes = [permissions.IsAuthenticated]

class PushTokenViewSet(viewsets.ModelViewSet):
    queryset = PushToken.objects.all()
    serializer_class = PushTokenSerializer
    permissions_classes = [permissions.IsAuthenticated]