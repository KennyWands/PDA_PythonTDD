import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Diamond", 2)
        self.card1 = Card("Spade", 1)
        self.game = CardGame()
        self.cards = [self.card, self.card1]

    def test_card_has_value(self):
        self.assertEquals(2, self.card.value)

    def test_card_has_suit(self):
        self.assertEqual("Diamond", self.card.suit)

    def test_for_Ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))

    def test_for_not_Ace(self):
        self.assertEqual(False, self.game.check_for_ace(self.card))

    def test_for_highest_card(self):
        self.assertEqual(self.card, self.game.highest_card(self.card, self.card1))

    def test_count_cards(self):
        self.assertEqual("You have a total of 3", self.game.cards_total(self.cards))
