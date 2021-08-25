import sqlite3
from django.shortcuts import render
from rater_reports.views import Connection
from rater_api.models import Game

def games_by_rating_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT g.title, AVG(r.rating) AS average_rating
                FROM rater_api_game AS g, rater_api_gamerating AS r
                WHERE g.id = r.game_id
                GROUP BY g.id
                ORDER BY average_rating DESC
                LIMIT 5;
            """)

            dataset = db_cursor.fetchall()
            games_by_rating = []

            for row in dataset:
                game = {}
                game["title"] = row["title"]
                game["average_rating"] = row["average_rating"]
                games_by_rating.append(game)
    
    template = 'games_by_rating.html'
    context = {
        'games_by_rating_list': games_by_rating
    }

    return render(request, template, context)