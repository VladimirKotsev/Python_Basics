import unittest

from Challenge5 import Х
from info import POSITION  # Поредният ви номер влиза магически

class TestLuck(unittest.TestCase):

    def test_luck(self):
        self.assertEqual(Х, POSITION)


if __name__ == '__main__':
    unittest.main()