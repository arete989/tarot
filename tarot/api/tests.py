import datetime
from freezegun import freeze_time
from unittest.mock import Mock

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from api.models import CrossReading
from api.views import CrossReadingCreate, CrossReadingById


class TestURLPatterns(TestCase):
    """
    TODO: This should be integrated with all of the test classes below
          and test with URLs intead of testing the class directly. But
          I don't have time to figure this out right now and this is
          sufficient for test coverage.

    https://stackoverflow.com/questions/35741090/how-to-test-url-in-django
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


@freeze_time('2023-10-10 00:00:00')
class TestCrossReadingById(TestCase):

    def setUp(self):
        self.reading1 = CrossReading(
            date_of_reading=datetime.date(2020, 1, 1),
            question_asked='What will happen?',
            pos1_card='empress',
            pos2_card='queen of swords',
            pos3_card='three of swords',
            pos4_card='hermit',
            pos5_card='lovers',
            pos6_card='ace of cups',
            pos7_card='two of pentacles',
            pos8_card='eight of pentacles',
            pos9_card='three of pentacles',
            pos10_card='ten of cups',
            pos6_mytake='a new passion is beginning',
            pos9_recap='this turned out to be accurate',
        )
        self.reading1.save()
        self.reading2 = CrossReading(
            date_of_reading=datetime.date(2023, 1, 1),
            question_asked='How will this turn out?',
            pos1_card='ten of pentacles',
            pos2_card='eight of pentacles',
            pos3_card='five of pentacles',
            pos4_card='nine of swords',
            pos5_card='nine of pentacles',
            pos6_card='eight of wands',
            pos7_card='page of swords',
            pos8_card='four of pentacles',
            pos9_card='wheel of fortune',
            pos10_card='high priestess',
            pos10_mytake='wait and see, future is unclear',
            pos3_recap='this did not happen',
        )
        self.reading2.save()

    def test_crossreadingbyid_get(self):
        request = Mock()
        pk = self.reading2.id

        response = CrossReadingById().get(request, pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'id': self.reading2.id,
            'created_at': datetime.datetime.now().strftime(("%Y-%m-%dT%H:%M:%SZ")),
            'modified_at': datetime.datetime.now().strftime(("%Y-%m-%dT%H:%M:%SZ")),
            'date_of_reading': str(self.reading2.date_of_reading),
            'question_asked': self.reading2.question_asked,
            'pos1_card': self.reading2.pos1_card,
            'pos2_card': self.reading2.pos2_card,
            'pos3_card': self.reading2.pos3_card,
            'pos4_card': self.reading2.pos4_card,
            'pos5_card': self.reading2.pos5_card,
            'pos6_card': self.reading2.pos6_card,
            'pos7_card': self.reading2.pos7_card,
            'pos8_card': self.reading2.pos8_card,
            'pos9_card': self.reading2.pos9_card,
            'pos10_card': self.reading2.pos10_card,
            'pos1_mytake': '',
            'pos2_mytake': '',
            'pos3_mytake': '',
            'pos4_mytake': '',
            'pos5_mytake': '',
            'pos6_mytake': '',
            'pos7_mytake': '',
            'pos8_mytake': '',
            'pos9_mytake': '',
            'pos10_mytake': self.reading2.pos10_mytake,
            'pos1_recap': '',
            'pos2_recap': '',
            'pos3_recap': self.reading2.pos3_recap,
            'pos4_recap': '',
            'pos5_recap': '',
            'pos6_recap': '',
            'pos7_recap': '',
            'pos8_recap': '',
            'pos9_recap': '',
            'pos10_recap': '',
        })
