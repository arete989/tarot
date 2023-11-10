from rest_framework import status
from rest_framework.exceptions import ValidationError
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
    This class contains the API views dealing with one CrossReading object.

    But `CrossReadingCreate` has to be separate from `CrossReadingById`
    because... why? Because this is the pattern followed in DRF tutorial
    but not sure I understand why they were split up into 2 different classes.
    Because the URL for each is different? But yes, usually the `Create`
    action is split off from R, U, D actions. #TODO
    """

    def post(self, request):
        serializer = CrossReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrossReadingById(APIView):
    """
    This class contains the API views dealing with one CrossReading object.
    Except for the `Create` action which is broken out separately.
    """
    def validate(self, pk):
        """
        DRF tutorial suggests calling this get_object but I'm calling
        it validate because I want to validate user auth in here as well.
        Unclear where that validation would happen automatically in DRF
        pattern. #TODO
        """
        try:
            self.reading = CrossReading.objects.get(pk=pk)
        except CrossReading.DoesNotExist:
            # DRF tutorial suggests raising django.http.Http404 here
            # But I'm raising ValidationError instead because it gives
            # more info about the error state to the API consumer
            # versus just a 404 - which helps the API consumer debug
            raise ValidationError('You are trying to access a reading that does not exist. Check the specified id.')

    def get(self, request, pk):
        self.validate(pk)
        serializer = CrossReadingSerializer(self.reading)
        return Response(serializer.data)

    def update(self, request, pk):  # TODO
        serializer = CrossReadingSerializer(self.reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.validate(pk)
        self.reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
