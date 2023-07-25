from django.urls import path
from .views import index, top_sellers, advertisement_post, register, login, profile, index

urlpatterns = [
    path("", index),
    path("top-sellers/", top_sellers, name="top_sellers"),
    path("advertisement-post/", advertisement_post, name="advertisement_post"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("index/", index, name="index"),
]