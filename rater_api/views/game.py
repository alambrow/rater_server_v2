from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rater_api.models.game import Game

class GameView(ViewSet):

    def list(self, request):
        """Handle GET"""
        games = Game.objects.all()
        serializer = GameSerializer(
            games, many=True, context={'request': request}
        )
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'number_of_players', 'est_time', 'age_rec')