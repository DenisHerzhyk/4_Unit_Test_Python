import unittest
from main import temp_list


class TestTemp(unittest.TestCase):
    def test_1(self):
        self.assertEqual(temp_list([22, 25, 18, 27, 23, 19, 20]), (22, 27, 18, 3, 4, 2))

    def test_2(self):
        self.assertEqual(temp_list([-5, -5, -5, -5, -5, -5, -5]), (-5, -5, -5, 0, 7, 6))

    def test_3(self):
        self.assertEqual(temp_list([30, 30, 30, 30, 30, 30, 30]), (30, 30, 30, 0, 7, 6))

    def test_4(self):
        self.assertEqual(temp_list([10, 20, 30, 40, 50, 60, 70]), (40, 70, 10, 3, 4, 6))

    def test_5(self):
        self.assertEqual(temp_list([0, 0, 0, 0, 0, 0, 0]), (0, 0, 0, 0, 7, 6))

    def test_6(self):
        self.assertEqual(temp_list([-10, -5, 0, 5, 10, 15, 20]), (5, 20, -10, 3, 4, 0))
