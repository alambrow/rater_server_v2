from django.http.response import HttpResponseServerError
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rater_api.models import Review, Player, Game

class ReviewView(ViewSet):
   
    def list(self, request):
        # reviews = Review.objects.all()

        # game = self.request.query_params.get('game', None)

        # if game is not None:
        #     reviews = reviews.filter(game=game)
        
        game = self.request.query_params.get('game', None)

        if game:
            reviews = Review.objects.filter(game=game)
        else:
            reviews = Review.objects.all()

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def create(self, request):
        review = Review()
        review.review = request.data["review"]

        player = Player.objects.get(user=request.auth.user)
        review.player = player

        game = Game.objects.get(pk=request.data["game"])
        review.game = game

        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1