# from rest_framework import generics
from .models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialazers import PostAPIfullSerialaser, CommentAPIfullSerialaser


class PostApipreview(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.preview)

    def put(self, request, post):
        parameter = request.GET.get('preview', '')
        model = Post.objects.get(id=post)
        model.preview = parameter
        model.save()
        return Response(model.preview)


class PostApititle(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.title)

    def put(self, request, post):
        parameter = request.GET.get('title', '')
        model = Post.objects.get(id=post)
        model.title = parameter
        model.save()
        return Response(model.title)


class PostApidislike(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.dislike)

    def put(self, request, post):
        parameter = request.GET.get('dislike', '')
        model = Post.objects.get(id=post)
        model.dislike = parameter
        model.save()
        return Response(model.dislike)


class PostApilike(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.like)

    def put(self, request, post):
        parameter = request.GET.get('like', '')
        model = Post.objects.get(id=post)
        model.like = parameter
        model.save()
        return Response(model.like)


class PostApicreated(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.created)


class PostApibody(APIView):
    def get(self, request, post):
        model = Post.objects.get(id=post)
        return Response(model.body)

    def put(self, request, post):
        parameter = request.GET.get('body', '')
        model = Post.objects.get(id=post)
        model.body = parameter
        model.save()
        return Response(model.body)


class PostAPIfull(APIView):

    def get(self, request, post):
        model = Post.objects.get(id=post)
        print(model)
        print(post)
        return Response(PostAPIfullSerialaser(model, many=False).data)

    def post(self, request, post):
        serializar = PostAPIfullSerialaser(data=request.data)
        serializar.is_valid()
        serializar.save()
        return Response({"Post": serializar.data})

    def delete(self, request, post):
        model = Post.objects.get(id=post)
        model.delete()
        return Response("Delete")

    def put(self, request, post):
        model = Post.objects.get(id=post)

        serializar = PostAPIfullSerialaser(data=request.data, instance=model)
        serializar.is_valid()
        serializar.save()
        return Response("PUT")


class CommentsAPIfull(APIView):
    def get(self, request, post):
        quantity = request.GET.get('count', '')    
        return Response(Comment.objects.filter(post_id=post)[:quantity])

    def delete(self, request, post):
        delete_comments = Comment.objects.get(id=post)
        delete_comments.delete() 
        return Response(delete_comments)

    def post(self, request, post):
        return 1
        # TODO: реалізуй пост метод у коментах