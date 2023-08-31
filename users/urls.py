from django.urls import path
from users.views import collect_user_information, success_page # noqa:  F401
from . import views

app_name = "users"

urlpatterns = [
    path(
        "collect-user-information/",
        views.collect_user_information,
        name="collect-user-information",
    ),
    path("success/", views.success_page, name="success"),
]
