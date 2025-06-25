from calculator import calculator
import unittest 

class testOperations(unittest.TestCase):

    def setUp(self):
        self.opertation = calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.opertation.get_sum(), 10, 'This is wrong')

    def test_get_multiple(self):
        self.assertEqual(self.opertation.get_multiple(), 16, 'This is wrong')

    def test_get_difference(self):
        self.assertEqual(self.opertation.get_difference(), 6, 'This is wrong')

    def test_get_division(self):
        self.assertEqual(self.opertation.get_quotient(), 4, 'This is wrong')

if __name__ == '__main__':
    unittest.main()