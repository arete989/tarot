from rest_framework import serializers
from api.models import CrossReading


class CrossReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrossReading
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
