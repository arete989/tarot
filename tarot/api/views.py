from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Card
from api.serializers import CardSerializer


"""
GENERAL PHILOSOPHY

This code is slightly more explicit than idiomatic code recommended by Django REST Framework (DRF) tutorial.
In particular, I avoided using mixins that come with DRF.
Because
    1) It hides too many operations behind the mixin abstraction. Makes it hard to debug without looking up documentation.
    2) Overreliance on mixins makes it harder to customize if you want to change one small detail of behavior.
    3) This code just isn't complex enough to warrant that level of abstraction. Saving 2 lines of code versus 4 lines.
"""


class GetCards(APIView):
    """
    This class contains all the API views dealing with an entire tarot deck
    An entire tarot deck is equivalent to all Cards in the database
    """

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        No `post` method written for now
        because the end user will never modify a deck
        """
        pass


class GetCard(APIView):
    """
    This class contains all the API views dealing with one Card object

    TODO: Maybe remove this class later
          Unclear if end user would ever need to retrieve one card at a time
          Would make more sense to fetch entire deck and store on frontend
          And manipulate through React
          No need to make so many requests for 1 card at a time
          Since the data stored in cards is essentially a constant
    """

    def validate(self, request, pk):
        try:
            self.card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise ValidationError('The card you requested does not exist')

    def get(self, request, pk):
        """
        Get one specific tarot card based on ID
        """
        self.validate(request, pk)

        serializer = CardSerializer(self.card)
        return Response(serializer.data)

    def post(self, request, pk):
        """
        No `post` method written for now
        because the end user will never modify a tarot card
        """
        pass
