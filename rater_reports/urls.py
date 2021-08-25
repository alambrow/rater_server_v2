from rater_reports.views.games.reverse_gamesbyrating import games_by_rating_list_reverse
from django.urls import path
from .views import games_by_rating_list, games_by_rating_list_reverse

urlpatterns = [
    path('reports/gamesbyrating', games_by_rating_list),
    path('reports/gamesbyratingreversed', games_by_rating_list_reverse),
]
