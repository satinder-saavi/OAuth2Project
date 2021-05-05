from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import (authentication, exceptions, viewsets, permissions, response, schemas)
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer, GroupSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from users.models import UserProfile
from rest_framework.decorators import api_view, action, renderer_classes



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ViewSets define the view behavior.

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class ExampleAuthentication(RetrieveAPIView, authentication.BaseAuthentication):
    serializer_class = UserSerializer
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)