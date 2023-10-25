from rest_framework import serializers
from api.models import Card


# TODO: Not convinced these serializers are actually needed
#       May be an unnecessary extra layer
#       Part of Django REST Framework boilerplate - try for now
#       Rip out later if they don't prove their value
#       Alternative: Just use the Django ORM directly
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'title', 'explanation']

    def create(self, validated_data):
        return Snippets.objects.create(**validated_data)