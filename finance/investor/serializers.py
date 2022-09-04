import rest_framework
from rest_framework.renderers import JSONRenderer

from .models import Post
from rest_framework import serializers


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
