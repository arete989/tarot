from rest_framework import serializers
from api.models import Card, ReadingCross


# TODO: Not convinced these serializers are actually needed
#       May be an unnecessary extra layer
#       Part of Django REST Framework boilerplate - try for now
#       Rip out later if they don't prove their value
#       Alternative: Just use the Django ORM directly
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'title', 'explanation']

    # TODO: More proof for ripping out this serializer
    # There is a bug below - use of `Snippets` - that was never caught
    # Because this code was never run. So it's not very useful.
    def create(self, validated_data):
        return Snippets.objects.create(**validated_data)


class ReadingCrossSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingCross
        fields = [
            'id',
            'created_at',
            'modified_at',
            'date_of_reading',
            'question_asked',
            'pos1_card',
            'pos2_card',
            'pos3_card',
            'pos4_card',
            'pos5_card',
            'pos6_card',
            'pos7_card',
            'pos8_card',
            'pos9_card',
            'pos10_card',
            'pos1_mytake',
            'pos2_mytake',
            'pos3_mytake',
            'pos4_mytake',
            'pos5_mytake',
            'pos6_mytake',
            'pos7_mytake',
            'pos8_mytake',
            'pos9_mytake',
            'pos10_mytake',
            'pos1_recap',
            'pos2_recap',
            'pos3_recap',
            'pos4_recap',
            'pos5_recap',
            'pos6_recap',
            'pos7_recap',
            'pos8_recap',
            'pos9_recap',
            'pos10_recap',
        ]
