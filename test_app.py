import unittest

from app import j_name


# class Test(TestCase):
#     def test_split_numbers(self):
#         # Given this
#         input = '3,5'
#         # When I did something
#         actual = split_numbers(input)
#         # I expect this Output
#         expected = ['3', '5']
#
#         self.assertEqual(actual, expected, "All ok")
#
#     def test_split(self):
#         self.fail()


class TestJname(unittest.TestCase):
    def test_j_name(self):
        input = 'anay'
        expected='katokafu'
        output=j_name(input)
        self.assertEqual(output,expected,"All Ok")

    def test_j_name1(self):
        input = '123'
        expected='Please check input'
        output=j_name(input)
        self.assertEqual(output,expected,"All Ok")

if __name__ == '__main__':
    unittest.main()
