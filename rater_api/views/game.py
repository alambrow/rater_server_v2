from django.http.response import HttpResponseServerError
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rater_api.models.game import Game
from rater_api.models.category import Category

class GameView(ViewSet):

    def list(self, request):
        """Handle GET for all game resources"""
        games = Game.objects.all()
        serializer = GameSerializer(
            games, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET for single Game resource
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def create(self, request):
        """Handles POST operations"""
        game = Game()
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.number_of_players = request.data["number_of_players"]
        game.est_time = request.data["est_time"]
        game.age_rec = request.data["age_rec"]

        cat = Category.objects.get(pk=request.data["category"])
        game.category = cat

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        depth = 1