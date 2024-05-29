from rest_framework import serializers
from .models import Post, Comment
# from rest_framework.response import Response
# class previewSerialaser(serializers.ModelSerializer):
#     model = Post
#     field = ("preview")


class PostAPIfullSerialaser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('preview', 'title', 'body', 'dislike', 'like', 'created')


class CommentAPIfullSerialaser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('creator', 'body', 'post')
