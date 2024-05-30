from django.urls import path
from account.views import CreateUserView, LoginUserView, ManageUserView, ManageUsersView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="get_token"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
    path("<int:pk>/", ManageUsersView.as_view(), name="manage_users"),
]

app_name = 'account'
