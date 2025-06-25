from calculator import calculator
import unittest 

class testOperations(unittest.TestCase):

    def test_sum(self):
        calculation = calculator(8,2)
        self.assertEqual(calculation.get_sum(), 10, 'This is wrong')

    def test_get_multiple(self):
        calculation = calculator(8,2)
        self.assertEqual(calculation.get_multiple(), 16, 'This is wrong')

    def test_get_difference(self):
        calculation = calculator(8,2)
        self.assertEqual(calculation.get_difference(), 6, 'This is wrong')

    def test_get_division(self):
        calculation = calculator(8,2)
        self.assertEqual(calculation.get_quotient(), 4, 'This is wrong')

if __name__ == '__main__':
    unittest.main()