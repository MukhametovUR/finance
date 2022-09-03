import rest_framework
from rest_framework.renderers import JSONRenderer

from .models import Post
from rest_framework import serializers


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post_id = validated_data.get("post_id", instance.post_id)
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_create = validated_data.get("time_create", instance.time_create)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance
