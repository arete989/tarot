import datetime
from unittest.mock import Mock

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from api.models import CrossReading
from api.views import CrossReadingCreate


class TestURLPatterns(TestCase):
    """
    TODO: This should be integrated with all of the test classes below
          and test with URLs intead of testing the class directly. But
          I don't have time to figure this out right now and this is
          sufficient for test coverage.
    """

    def test_crossreading_url(self):
        pass


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
        """
        The data sent here is the minimum required amount of data.
        """
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
        # Also check that it didn't randomly fill out fields that were not populated
        self.assertEqual(reading.pos7_mytake, '')
        self.assertEqual(reading.pos10_recap, '')

    def test_crossreadingcreate_fulldata(self):
        """
        Success case with more data than the required minimum.
        """
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)

        request = Mock()
        request.data = self.cross_reading.copy()
        # This is extra data beyond the required minimum
        request.data['pos6_mytake'] = 'A new passion that is beginning'
        request.data['pos8_recap'] = '6 months later this turned out to be correct'

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
        # Make sure that extra data that I sent was populated
        self.assertEqual(reading.pos6_mytake, request.data['pos6_mytake'])
        self.assertEqual(reading.pos8_recap, request.data['pos8_recap'])
        # And that fields I did NOT send were NOT populated
        self.assertEqual(reading.pos7_mytake, '')
        self.assertEqual(reading.pos10_recap, '')

    def test_crossreadingcreate_missingdata(self):
        """
        Missing some of the required minimum fields. Should raise error.
        """
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)

        request = Mock()
        request.data = self.cross_reading.copy()
        del request.data['pos1_card']  # Remove one of the required fields

        response = CrossReadingCreate().post(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['pos1_card'][0].code, 'required')

        # Make sure that nothing was created in the database
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)

    def test_crossreadingcreate_invaliddata(self):
        """
        One of the fields passed for the card is not valid. Should raise error.
        """
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)

        request = Mock()
        request.data = self.cross_reading.copy()
        request.data['pos5_card'] = 'not a real card name'

        response = CrossReadingCreate().post(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['non_field_errors'][0]), 'This is not a valid tarot card name')

        # Make sure that nothing was created in the database
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 0)
