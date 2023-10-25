from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Card
from api.serializers import CardSerializer


# SECURITY TODO: Remove this @csrf_exempt later
#                See DRF tutorial for full explanation
@csrf_exempt
def get_all_cards(request):

    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return JsonResponse(serializer.data, safe=False)


# SECURITY TODO: Remove this @csrf_exempt later
#                See DRF tutorial for full explanation
@csrf_exempt
def get_one_card(request, pk):

    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CardSerializer(card)
        return JsonResponse(serializer.data, safe=False)

