import unittest
from Week6B.max import max


class MaxTestCase(unittest.TestCase):

    def test_Max_FirstIsGreater_returnFirst(self):
        self.assertEqual(2, max(2, 1))

    def test_Max_SecondIsGreater_returnSecond(self):
        self.assertEqual(2, max(1, 2))

    def test_Max_Equals_returnAny(self):
        self.assertEqual(2, max(2, 2))

    def test_Max_FirstIsGreaterAndNegative_returnFirst(self):
        self.assertEqual(-1, max(-1, -2))

    def test_Max_SecondIsGreaterAndNegative_returnSecond(self):
        self.assertEqual(-1, max(-2, -1))

    def test_Max_EqualsAndNegative_returnAny(self):
        self.assertEqual(-2, max(-2, -2))


if __name__ == '__main__':
    unittest.main()
