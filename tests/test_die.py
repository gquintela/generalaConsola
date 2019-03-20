from unittest import TestCase, main

from generala.die import Die

class TestDie(TestCase):

    def test_init_dice_amount(self):
        die = Die()
        self.assertEqual(die.value, 0)
        self.assertEqual(die.status, False)


if __name__ == '__main__':
    main()

