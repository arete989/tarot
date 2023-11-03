from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import CrossReading
from api.serializers import CrossReadingSerializer


"""

This code is slightly more verbose than idiomatic code recommended
by Django REST Framework (DRF) tutorial. In particular, I avoided
using class mixins that come with DRF. Because

    1) It hides too many operations behind the mixin abstraction.
       Makes it hard to debug without looking up documentation.
    2) Overreliance on mixins makes it harder to customize if you
       want to change one small detail of behavior.
    3) This code just isn't complex enough to warrant that level
       of abstraction. Saving 2 lines of code versus 4 lines.

"""


class CrossReadingCreate(APIView):
    """
    TODO: Clean up explanation below
    This class contains the API view dealing with one ReadingCross object
    For only the 'Create' action
    I don't get why this is a separate class from 'Retrieve', 'Update', 'Delete'
    Or included in the same class as ReadingCrossList per the DRF tutorial
    """

    def validate(self, request):  # TODO: fill out
        # TODO: if I'm going to use a serializer, this should
        # be in the serializer
        pass

    def post(self, request):
        serializer = CrossReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrossReadingById(APIView):
    """
    TODO: Docstring. Comparison versus above.
    """

    def validate(self, request):  # TODO
        pass

    def get(self, request, pk):  # TODO
        pass

    def update(self, request, pk):  # TODO
        pass

    def delete(self, request, pk):  # TODO
        pass
