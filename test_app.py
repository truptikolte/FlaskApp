from unittest import TestCase

from app import split_numbers


class Test(TestCase):
    def test_split_numbers(self):
        # Given this
        input = '3,5'
        # When I did something
        actual = split_numbers(input)
        # I expect this Output
        expected = ['3', '5']

        self.assertEqual(actual, expected, "All ok")
