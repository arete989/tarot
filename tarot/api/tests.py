import datetime
from unittest.mock import Mock

from django.test import TestCase

from api.models import CrossReading
from api.views import CrossReadingCreate


class TestCrossReadingCreate(TestCase):

    # TODO: Build out this test class and standardize naming

    def setUp(self):
        self.date_of_reading = datetime.date(2020, 1, 1)
        self.question_asked = 'What will happen?'
        self.pos1_card = 'queen of swords'
        self.pos2_card = 'queen of swords'
        self.pos3_card = 'queen of swords'
        self.pos4_card = 'queen of swords'
        self.pos5_card = 'queen of swords'
        self.pos6_card = 'queen of swords'
        self.pos7_card = 'queen of swords'
        self.pos8_card = 'queen of swords'
        self.pos9_card = 'queen of swords'
        self.pos10_card = 'queen of swords'

    def test_crossreadingcreate_success(self):
        
        # TODO: Build out this test case, look at jelly/api/tests/test_views.py for reference

        request = Mock()
        request.data = {
            'date_of_reading': self.date_of_reading,
            'question_asked': self.question_asked,
            'pos1_card': self.pos1_card,
            'pos2_card': self.pos2_card,
            'pos3_card': self.pos3_card,
            'pos4_card': self.pos4_card,
            'pos5_card': self.pos5_card,
            'pos6_card': self.pos6_card,
            'pos7_card': self.pos7_card,
            'pos8_card': self.pos8_card,
            'pos9_card': self.pos9_card,
            'pos10_card': self.pos10_card,
        }

        response = CrossReadingCreate().post(request)
        self.assertEqual(response.status_code, 201)
