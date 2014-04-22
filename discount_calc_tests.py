import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	"""class wrapper for testing if Discount_calc works"""
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 10, 'percent')
		self.assertEqual(10, result)

	def test_fifteen_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 15, 'percent')
		self.assertEqual(15, result)

	def test_five_dollar_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(250, 5, 'absolute')
		self.assertEqual(5, result)

	def test_invalid_discount_type_raises_value_error(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 5, 'random')