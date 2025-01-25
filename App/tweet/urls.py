
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.tweet_list, name="tweet_list"),
    path("createTweet/", views.create_tweet, name="tweet_create"),
    path("searchTweet/", views.search_tweet, name="search_tweet"),
    path("<int:tweet_id>/tweet_edit/", views.edit_tweet, name="tweet_edit"),
    path("<int:tweet_id>/tweet_delete/", views.delete_tweet, name="tweet_delete"),
    path("register/", views.register, name="register"),
] 
