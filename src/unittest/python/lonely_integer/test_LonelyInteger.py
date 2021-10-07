from unittest import TestCase

from src.main.python.lonely_integer.LonelyInteger import lonelyinteger


class Test(TestCase):
    def test_lonelyinteger(self):
        input_data = [1, 2, 3, 4, 3, 2, 1]
        output = lonelyinteger(input_data)

        self.assertEqual(4, output)

    def test_lonelyinteger_ii(self):
        input_data = [0, 0, 1, 2, 1, 5, 5]
        output = lonelyinteger(input_data)

        self.assertEqual(2, output)

    def test_lonelyinteger_single_number_list(self):
        input_data = [0]
        output = lonelyinteger(input_data)

        self.assertEqual(0, output)
