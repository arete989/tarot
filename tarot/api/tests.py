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

    def test_crossreadingbyid_get_success(self):
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

    def test_crossreadingbyid_get_invalidpk(self):
        request = Mock()
        pk = self.reading1.id + 100

        with self.assertRaises(ValidationError) as e:
            response = CrossReadingById().get(request, pk)

        self.assertEqual(
            e.exception.args[0],
            'You are trying to access a reading that does not exist. Check the specified id.',
        )

    def test_crossreadingbyid_update_success(self):
        reading_original = CrossReading.objects.get(pk=self.reading2.id)
        self.assertEqual(reading_original.question_asked, self.reading2.question_asked)
        self.assertEqual(reading_original.pos3_card, self.reading2.pos3_card)
        self.assertEqual(reading_original.pos3_recap, self.reading2.pos3_recap)
        self.assertEqual(reading_original.pos10_recap, self.reading2.pos10_recap)

        request = Mock()
        pk = self.reading2.id
        # Update the value for pos3_card
        # Add a value for pos10_recap which was blank before
        # Nothing else is changed
        # Need to send the entire object again for idempotency
        updated_pos3_card = 'five of cups'
        updated_pos10_recap = 'reevaluating this 6 months later'
        request.data = {
            'date_of_reading': self.reading2.date_of_reading,
            'question_asked': self.reading2.question_asked,
            'pos1_card': self.reading2.pos1_card,
            'pos2_card': self.reading2.pos2_card,
            'pos3_card': updated_pos3_card,
            'pos4_card': self.reading2.pos4_card,
            'pos5_card': self.reading2.pos5_card,
            'pos6_card': self.reading2.pos6_card,
            'pos7_card': self.reading2.pos7_card,
            'pos8_card': self.reading2.pos8_card,
            'pos9_card': self.reading2.pos9_card,
            'pos10_card': self.reading2.pos10_card,
            'pos10_recap': updated_pos10_recap,
        }

        """
        TODO: This brings up a bigger issue of API and schema design.
              If idempotent - how should we handle the fact that for
              a given Reading - optional fields like _mytake, _recap
              may be populated in the existing object - but when updating
              the API consumer is not required to send those fields.
              This would result in no idempotency (?). So should we always
              require all fields to be sent? And if a field is default
              blank, require the API consumer to send a blank value? Need
              to do more research on how to handle this.

              This needs to be resolved - it seems like an edge case but
              is the kind of thing that would lead to really weird timing
              bugs in the future and be really hard to debug.
        """

        response = CrossReadingById().put(request, pk)
        self.assertEqual(response.status_code, 200)

        # Check that object was correctly updated in DB
        reading_updated = CrossReading.objects.get(pk=pk)
        self.assertEqual(reading_updated.question_asked, reading_original.question_asked)
        self.assertEqual(reading_updated.pos3_card, updated_pos3_card)
        self.assertEqual(reading_updated.pos3_recap, reading_original.pos3_recap)
        self.assertEqual(reading_updated.pos10_recap, updated_pos10_recap)

        # TODO: Should also check that `modified_at` was correctly updated
        #       Test this using `freeze_time`

    def test_crossreadingbyid_update_invalidpk(self):
        request = Mock()
        pk = self.reading1.id + 100

        with self.assertRaises(ValidationError) as e:
            response = CrossReadingById().put(request, pk)

        self.assertEqual(
            e.exception.args[0],
            'You are trying to access a reading that does not exist. Check the specified id.',
        )

    def test_crossreadingbyid_update_invaliddata(self):
        reading_original = CrossReading.objects.get(pk=self.reading2.id)
        self.assertEqual(reading_original.question_asked, self.reading2.question_asked)
        self.assertEqual(reading_original.pos3_card, self.reading2.pos3_card)
        self.assertEqual(reading_original.pos3_recap, self.reading2.pos3_recap)
        self.assertEqual(reading_original.pos10_recap, self.reading2.pos10_recap)

        request = Mock()
        pk = self.reading2.id
        request.data = {
            'date_of_reading': self.reading2.date_of_reading,
            'question_asked': self.reading2.question_asked,
            'pos1_card': self.reading2.pos1_card,
            'pos2_card': self.reading2.pos2_card,
            'pos3_card': 'not a valid card name',
            'pos4_card': self.reading2.pos4_card,
            'pos5_card': self.reading2.pos5_card,
            'pos6_card': self.reading2.pos6_card,
            'pos7_card': self.reading2.pos7_card,
            'pos8_card': self.reading2.pos8_card,
            'pos9_card': self.reading2.pos9_card,
            'pos10_card': self.reading2.pos10_card,
        }

        response = CrossReadingById().put(request, pk)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['non_field_errors'][0]), 'This is not a valid tarot card name')

        # Check that nothing was modified in the DB
        reading_updated = CrossReading.objects.get(pk=pk)
        self.assertEqual(reading_updated.question_asked, reading_original.question_asked)
        self.assertEqual(reading_updated.pos3_card, reading_original.pos3_card)
        self.assertEqual(reading_updated.pos3_recap, reading_original.pos3_recap)
        self.assertEqual(reading_updated.pos10_recap, reading_original.pos10_recap)

    def test_crossreadingbyid_update_missingdata(self):
        reading_original = CrossReading.objects.get(pk=self.reading2.id)
        self.assertEqual(reading_original.question_asked, self.reading2.question_asked)
        self.assertEqual(reading_original.pos3_card, self.reading2.pos3_card)
        self.assertEqual(reading_original.pos3_recap, self.reading2.pos3_recap)
        self.assertEqual(reading_original.pos10_recap, self.reading2.pos10_recap)

        request = Mock()
        pk = self.reading2.id
        request.data = {
            'date_of_reading': self.reading2.date_of_reading,
            'question_asked': self.reading2.question_asked,
            'pos1_card': self.reading2.pos1_card,
            'pos2_card': self.reading2.pos2_card,
            # data for pos3_card is missing
            # even though the existing object in DB is populated
            # this should still raise an error because the field is required to be sent
            # for idempotency
            'pos4_card': self.reading2.pos4_card,
            'pos5_card': self.reading2.pos5_card,
            'pos6_card': self.reading2.pos6_card,
            'pos7_card': self.reading2.pos7_card,
            'pos8_card': self.reading2.pos8_card,
            'pos9_card': self.reading2.pos9_card,
            'pos10_card': self.reading2.pos10_card,
        }

        response = CrossReadingById().put(request, pk)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['pos3_card'][0].code, 'required')

        # Check that nothing was modified in the DB
        reading_updated = CrossReading.objects.get(pk=pk)
        self.assertEqual(reading_updated.question_asked, reading_original.question_asked)
        self.assertEqual(reading_updated.pos3_card, reading_original.pos3_card)
        self.assertEqual(reading_updated.pos3_recap, reading_original.pos3_recap)
        self.assertEqual(reading_updated.pos10_recap, reading_original.pos10_recap)

    def test_crossreadingbyid_delete_success(self):
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 2)

        request = Mock()
        pk = self.reading1.id

        response = CrossReadingById().delete(request, pk)
        self.assertEqual(response.status_code, 204)

        # Check that reading1 was deleted and reading2 is still there
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 1)
        self.assertEqual(readings[0].id, self.reading2.id)

    def test_crossreadingbyid_delete_invalidpk(self):
        """
        This is why test driven development is important.
        Originally I thought this test case was redundant/overkill.
        But it wasn't until I wrote this test case that I realized
        I had forgotten to write the code for validation.
        """
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 2)

        request = Mock()
        pk = self.reading1.id + 100

        with self.assertRaises(ValidationError) as e:
            response = CrossReadingById().delete(request, pk)

        self.assertEqual(
            e.exception.args[0],
            'You are trying to access a reading that does not exist. Check the specified id.',
        )

        # Check that nothing was deleted in the DB
        readings = CrossReading.objects.all()
        self.assertEqual(readings.count(), 2)
