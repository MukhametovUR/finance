from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Post, Category
from .serializers import PostSerializer


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly, )
