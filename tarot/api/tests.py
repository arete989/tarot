import datetime
from unittest.mock import Mock

from django.test import TestCase

from api.models import CrossReading
from api.views import CrossReadingCreate


class TestCrossReadingCreate(TestCase):

    def setUp(self):
        self.cross_reading = {
            'date_of_reading': datetime.date(2020, 1, 1),
            'question_asked': 'What will happen?',
            'pos1_card': 'empress',
            'pos2_card': 'queen of swords',
            'pos3_card': 'three of swords',
            'pos4_card': 'hermit',
            'pos5_card': 'lovers',
            'pos6_card': 'ace of cups',
            'pos7_card': 'two of pentacles',
            'pos8_card': 'eight of pentacles',
            'pos9_card': 'three of pentacles',
            'pos10_card': 'ten of cups',
        }

    def test_crossreadingcreate_success(self):
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)

        request = Mock()
        request.data = self.cross_reading

        response = CrossReadingCreate().post(request)
        self.assertEqual(response.status_code, 201)

        # Make sure that CrossReading object was correctly created in DB
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 1)
        reading = readings[0]
        self.assertEqual(reading.date_of_reading, self.cross_reading['date_of_reading'])
        self.assertEqual(reading.question_asked, self.cross_reading['question_asked'])
        self.assertEqual(reading.pos1_card, self.cross_reading['pos1_card'])
        self.assertEqual(reading.pos2_card, self.cross_reading['pos2_card'])
        self.assertEqual(reading.pos3_card, self.cross_reading['pos3_card'])
        self.assertEqual(reading.pos4_card, self.cross_reading['pos4_card'])
        self.assertEqual(reading.pos5_card, self.cross_reading['pos5_card'])
        self.assertEqual(reading.pos6_card, self.cross_reading['pos6_card'])
        self.assertEqual(reading.pos7_card, self.cross_reading['pos7_card'])
        self.assertEqual(reading.pos8_card, self.cross_reading['pos8_card'])
        self.assertEqual(reading.pos9_card, self.cross_reading['pos9_card'])
        self.assertEqual(reading.pos10_card, self.cross_reading['pos10_card'])

    def test_crossreadingcreate_url(self):
        pass  # TODO
        # put this in a separate class?








