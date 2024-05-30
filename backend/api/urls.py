from rest_framework import routers

from django.urls import path, include
from api import views

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('comments/', views.CommentViewSet.as_view()),
]

app_name = "api"
