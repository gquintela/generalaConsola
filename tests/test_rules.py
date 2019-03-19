from unittest import TestCase, main
from generala.beaker import Beaker
from generala.rules import Rules

class TestRules(TestCase):

    def test_number_count(self):
        rules = Rules()
        beaker = Beaker()
        for die in beaker.dice:
            die.value = 1
        self.assertEqual(rules.number_count(beaker,1),5)
        for die in range(5):
            beaker.dice[die].value = die + 1
        self.assertEqual(rules.number_count(beaker,die + 1),die + 1)

