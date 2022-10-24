import rest_framework
from rest_framework.renderers import JSONRenderer

from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"
