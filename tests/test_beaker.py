from unittest import TestCase, main
from generala.die import Die

from generala.beaker import Beaker


class TestBeaker(TestCase):

    def test_init_dice_amount(self):
        beaker = Beaker()
        self.assertEqual(len(beaker.dice), 5)

    def test_init_dice_unlocked(self):
        beaker = Beaker()
        self.assertEqual(all(die.status for die in beaker.dice),0)

    def test_lock_dice(self):
        beaker = Beaker()
        dice = [1,2,3,4,5]
        beaker.lock_dice(dice)
        self.assertEqual(all(die.status for die in beaker.dice), 1)

    def test_throw_beaker_all_unlocked(self):
        beaker = Beaker()
        beaker.throw_beaker()
        self.assertEqual(all(die.status for die in beaker.dice), 0)

    def test_throw_beaker_locked(self):
        beaker = Beaker()
        beaker.lock_dice([1,2,3,4,5])
        test_beaker=beaker
        self.assertEqual(beaker, test_beaker)
        beaker.throw_beaker()
        self.assertEqual(beaker, test_beaker)

    def test_sort(self):
        beaker = Beaker()
        die1 = Die()
        die2 = Die()
        die3 = Die()
        die4 = Die()
        die5 = Die()
        test_dice = [die1,die2,die3,die4,die5]
        beaker.dice = test_dice
        beaker.sort()
        for die in range(4):
            self.assertTrue(beaker.dice[die].value <= beaker.dice[die + 1].value)


if __name__ == '__main__':
    main()
