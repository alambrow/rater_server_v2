from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rater_api.models import GameRating, Player, Game

class RatingView(ViewSet):

    def list(self, request):
        game = self.request.query_params.get('game', None)

        if game:
            ratings = GameRating.objects.filter(game=game)
        else:
            ratings = GameRating.objects.all()

        serial = RatingSerializer(
            ratings, many=True, context={'request': request}
        )
        return Response(serial.data)
    
    def create(self, request):
        rating = GameRating()
        rating.rating = request.data["rating"]
        player = Player.objects.get(user=request.auth.user)
        rating.player = player
        game = Game.objects.get(pk=request.data["game"])
        rating.game = game

        try:
            rating.save()
            serial = RatingSerializer(rating, context={'request': request})
            return Response(serial.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRating
        fields = '__all__'
        depth = 1