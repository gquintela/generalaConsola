from unittest import TestCase, main
from generala.player import Player


class TestPlayer(TestCase):

    def test_init_player(self):
        player = Player()
        self.assertEqual(player.name, "")
        for key in player.categories:
            self.assertEqual(player.categories[key], None)


    def test_sum_total_points(self):
        pass #TODO

