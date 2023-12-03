import unittest
from seminar3.main_hw import MainHW


class HWTest(unittest.TestCase):
    def test_even_odd_number_test(self):
        self.assertTrue(MainHW.even_odd_number(10))
        self.assertFalse(MainHW.even_odd_number(11))

    def test_number_in_interval(self):
        self.assertTrue(MainHW.number_in_interval(30))
        self.assertFalse(MainHW.number_in_interval(10))
