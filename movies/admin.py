from django.contrib import admin
from .models import Movie, Review, Rating, WatchList

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(WatchList)