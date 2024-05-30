from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication

from api.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
from custom_permission import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user_id = self.request.query_params.get('author_id', None)
        if user_id:
            return Post.objects.filter(author_id=user_id)
        return Post.objects.all()


class CommentViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        return Comment.objects.filter(post_id=post_id)
