from django.shortcuts import render
from .models import Movie, Viewer, Review


def home(request):
    context = {
        "movie_exact": Movie.objects.filter(title__exact="Inception"),

        "viewers_contains_lastname": Viewer.objects.filter(last_name__contains="Mel"),

        "genre_starts": Movie.objects.filter(genre__startswith="Sci"),

        "email_ends": Viewer.objects.filter(email__endswith="@gmail.com"),

        "long_movies": Movie.objects.filter(duration_minutes__gt=120),

        "high_score_reviews": Review.objects.filter(score__gte=8),

        "low_rating_movies": Movie.objects.filter(rating__lt=5),

        "young_viewers": Viewer.objects.filter(age__lte=18),

        "medium_length_movies": Movie.objects.filter(
            duration_minutes__range=(90, 150)
        ),

        "movies_in_list": Movie.objects.filter(id__in=[1, 3, 7]),

        "reviews_without_viewer": Review.objects.filter(viewer__isnull=True),
    }

    return render(request, "movies/home.html", context)
