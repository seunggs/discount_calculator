import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	"""class wrapper for testing if Discount_calc works"""
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 10, 'percent')
		self.assertEqual(10, result)