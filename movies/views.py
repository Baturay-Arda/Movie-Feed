from django.shortcuts import render, redirect
from .models import Movie, Review, Rating, WatchList
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@login_required
def movie_list(request):
    query = request.GET.get('q')

    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, 'movies/movie_list.html', {'movies': movies})    

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)

    avg_rating = movie.ratings.aggregate(Avg('score'))['score__avg']
        
    context = {
        'movie': movie,
        'avg_rating': avg_rating
    }

    return render(request, 'movies/movie_detail.html', context)

@login_required
def add_review(request, pk):
    movie = Movie.objects.get(id=pk)

    if request.method == 'POST':
        Review.objects.create(
            user=request.user,
            movie=movie,
            text=request.POST.get('text')
        )
    return redirect('movie_detail', pk=pk)

@login_required
def toggle_watchlist(request, pk):
    movie = Movie.objects.get(id=pk)

    obj, created = WatchList.objects.get_or_create(
        user=request.user,
        movie=movie
    )

    if not created:
        obj.delete()

    return redirect('movie_detail', pk=pk)

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, id=pk)

    if review.user == request.user:
        review.delete()

    return redirect('movie_detail', pk=review.movie.id)

@login_required
def add_rating(request, pk):
    movie = Movie.objects.get(id=pk)
    score = request.POST.get('score')
    if score:
        score = int(score)

    Rating.objects.update_or_create(
        user=request.user,
        movie=movie,
        defaults={'score': score}
    )

    return redirect('movie_detail', pk=pk)

@login_required
def watchlist(request):
    movies = Movie.objects.filter(watchlist__user=request.user)

    return render(request, 'movies/watchlist.html', {'movies': movies})

@login_required
def add_review_ajax(request, pk):
    if request.method == "POST":
        movie = Movie.objects.get(id=pk)
        text = request.POST.get('text')

        review = Review.objects.create(
            user=request.user,
            movie=movie,
            text=text
        )

        return JsonResponse({
            'user': request.user.username,
            'text': review.text
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)