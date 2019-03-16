from unittest import TestCase

from ..generala import *
from ..generala import Beaker

testBeaker01 = Beaker()
testBeaker01[0][1] = 1
testBeaker01[1][1] = 1
testBeaker01[2][1] = 1
testBeaker01[3][1] = 3
testBeaker01[4][1] = 3


class TestGame(TestCase):
    def test_computeNumberCount(self):
        self.fail()

