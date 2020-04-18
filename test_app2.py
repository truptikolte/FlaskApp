import unittest

from app import j_name


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_j_name(self):
        input = 'anay'
        expected='katokafu'
        output=j_name(input)
        self.assertEqual(output,expected,"All Ok")


if __name__ == '__main__':
    unittest.main()
