from unittest.mock import Mock

from django.test import TestCase

from rest_framework.exceptions import ValidationError

from api.models import Card
from api.views import (
    GetCard,
    GetCards,
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
