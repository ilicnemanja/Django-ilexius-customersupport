from os import name
from django.urls import path

from .views import *

app_name = "support"

urlpatterns = [
    path("", customer_support, name="customer_support"),
    path("check-support", check_support, name="check_support"),
    path("view_list", view_list, name="view_list"),
    path("view_detail/<int:customer_id>", view_detail, name="view_detail"),
    path("add-to-archive/<int:customer_id>", add_to_archive, name="add_to_archive"),
    path("view_archived_list", view_archived_list, name="view_archived_list"),
    path("restore/<int:customer_id>", restore, name="restore"),
    path("delete/<int:customer_id>", delete, name="delete"),
    path("view_detail/<int:customer_id>/add-comment", add_comment, name="add_comment"),
    path("register-user", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
]