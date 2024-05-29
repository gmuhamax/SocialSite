from django.urls import path
from api.views import (PostApipreview, PostApititle, PostApibody,
                       PostApilike, PostApidislike, PostAPIfull,
                       PostApicreated, CommentsAPIfull)

urlpatterns = [

    path('post/<int:post>/', PostAPIfull.as_view()),
    path('post/<int:post>/title', PostApititle.as_view()),
    path('post/<int:post>/body', PostApibody.as_view()),
    path('post/<int:post>/like', PostApilike.as_view()),
    path('post/<int:post>/dislike', PostApidislike.as_view()),
    path('post/<int:post>/preview', PostApipreview.as_view()),
    path('post/<int:post>/created', PostApicreated.as_view()),
    path('post/<int:post>/comments', CommentsAPIfull.as_view())
]
app_name = "api"
