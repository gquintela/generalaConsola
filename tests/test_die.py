from unittest import TestCase, main
from generala.beaker import Beaker

from generala.die import Die

class TestDie(TestCase):

    def test_init_dice_amount(self):
        die = Die()
        self.assertEqual(die.value, 0)
        self.assertEqual(die.status, 0)