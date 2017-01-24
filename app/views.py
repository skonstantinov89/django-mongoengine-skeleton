from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status, response, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from clients.models import *


User = get_user_model()

# Create your views here.

# Sample usage
class TaskView(views.APIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        x = Tasks.objects(title='test')[0].to_json()
        return HttpResponse(x, content_type='application/json')


class UserView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    # serializer_class = serializers.serializers_manager.get('user')
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self, *args, **kwargs):
        return self.request.user
