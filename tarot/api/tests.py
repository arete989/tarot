import datetime
from unittest.mock import Mock

from django.test import TestCase

from rest_framework.exceptions import ValidationError

from api.models import (
    Card,
    ReadingCross,
)
from api.views import (
    GetCard,
    GetCards,
    ReadingCrossCreate,
)


class TestGetCards(TestCase):

    def setUp(self):
        self.card1 = Card(
            title='Queen of Swords',
            explanation='archetype of an older, wiser feminine intellect',
        )
        self.card1.save()
        self.card2 = Card(
            title='Queen of Pentacles',
            explanation='down to earth, practical, thrify',
        )
        self.card2.save()

    def test_get_cards_success_case(self):
        request = Mock()
        response = GetCards().get(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {
                'id': self.card1.id,
                'title': self.card1.title,
                'explanation': self.card1.explanation,
            },
            {
                'id': self.card2.id,
                'title': self.card2.title,
                'explanation': self.card2.explanation,

            },
        ])


class TestGetCard(TestCase):

    def setUp(self):
        self.card1 = Card(
            title='Queen of Swords',
            explanation='archetype of an older, wiser feminine intellect',
        )
        self.card1.save()
        self.card2 = Card(
            title='Queen of Pentacles',
            explanation='down to earth, practical, thrify',
        )
        self.card2.save()

    def test_get_card_success_case(self):
        request = Mock()
        card_id = self.card2.id

        response = GetCard().get(request, card_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'id': self.card2.id,
            'title': self.card2.title,
            'explanation': self.card2.explanation,

        })

    def test_get_card_with_invalid_card_id(self):
        request = Mock()
        card_id = self.card2.id + 1

        with self.assertRaises(ValidationError) as e:
            response = GetCard().get(request, card_id)

        self.assertEqual(
            e.exception.args[0],
            'The card you requested does not exist',
        )


class TestReadingCrossCreate(TestCase):

    # TODO: Refine this test case and standardize naming

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

    def test_readingcrosscreate_success_case(self):
        
        # TODO: Improve this test case, look at jelly/api/tests/test_views.py for reference

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

        response = ReadingCrossCreate().post(request)

        import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 201)








