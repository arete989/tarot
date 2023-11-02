from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import (
    Card,
    ReadingCross,
)
from api.serializers import CardSerializer, ReadingCrossSerializer


"""
GENERAL PHILOSOPHY

This code is slightly more explicit than idiomatic code recommended by Django REST Framework (DRF) tutorial.
In particular, I avoided using mixins that come with DRF.
Because
    1) It hides too many operations behind the mixin abstraction. Makes it hard to debug without looking up documentation.
    2) Overreliance on mixins makes it harder to customize if you want to change one small detail of behavior.
    3) This code just isn't complex enough to warrant that level of abstraction. Saving 2 lines of code versus 4 lines.
"""


# TODO: Rename? CardList
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

        TODO: Does that mean the Card model is better stored as a constant?
        """
        pass


# TODO: Rename? CardById
class GetCard(APIView):
    """
    This class contains all the API views dealing with one Card object

    TODO: Maybe remove this class later
          Unclear if end user would ever need to retrieve one card at a time
          Would make more sense to fetch entire deck and store on frontend
          And manipulate through React
          No need to make so many requests for 1 card at a time
          Since the data stored in cards is essentially a constant

    TODO: Does that mean the Card model is better stored as a constant?
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


class ReadingCrossCreate(APIView):
    """
    This class contains the API view dealing with one ReadingCross object
    For only the 'Create' action
    I don't get why this is a separate class from 'Retrieve', 'Update', 'Delete'
    Or included in the same class as ReadingCrossList per the DRF tutorial
    TODO: Revisit code organization for this
    """

    def validate(self, request):  # TODO: fill out
        # TODO: if I'm going to use a serializer, this should
        # be in the serializer
        pass

    def post(self, request):
        serializer = ReadingCrossSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadingCrossById(APIView):
    """
    This class contains all the API views dealing with one ReadingCross object.

    TODO: I don't like overloading this class name to be the same as the model name
    Though I understand DRF philosophy is that endpoints basically map to CRUD of models
    I think it gets confusing in a large codebase when someone just searches for `TarotReadingCelticCross`
    I would prefer naming this something like `APITarotReadingCelticCross` or `TouchTarotReadingCelticCross`
    But maybe this naming convention is a standard pattern that's clear enough for anyone who works extensively with DRF...
    """

    def validate(self, request):  # TODO
        pass

    def get(self, request, pk):  # TODO
        pass

    def update(self, request, pk):  # TODO
        pass

    def delete(self, request, pk):  # TODO
        pass
