from django.db import models
from account.models import User


class Post(models.Model):
    preview = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    body = models.TextField()
    dislike = models.IntegerField()
    like = models.IntegerField()
    created = models.DateField(auto_now_add=True)

 
class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
