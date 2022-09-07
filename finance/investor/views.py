from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Post, Category
from .serializers import PostSerializer


class PostViewSet( mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   # mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        pk=self.kwargs.get("pk")

        if not pk:
            return Post.objects.all()[:3]

        return Post.objects.filter(pk=pk)



    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})


# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
