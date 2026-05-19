from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),

    path(
        '<int:pk>/',
        views.movie_detail,
        name='movie_detail'
    ),

    path(
        '<int:pk>/watchlist/',
        views.toggle_watchlist,
        name='toggle_watchlist'
    ),

    path(
        '<int:pk>/rate/',
        views.add_rating,
        name='add_rating'
    ),

    path(
        'watchlist/',
        views.watchlist,
        name='watchlist'
    ),

    path(
        '<int:pk>/review/',
        views.add_review,
        name='add_review'
    ),
]