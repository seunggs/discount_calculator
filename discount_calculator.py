
class DiscountCalculator(object):
	def calculate(self, total, discount_amount, discount_type):
		if discount_type == "percent":
			percentage_discount = float(discount_amount) / 100
			discount = percentage_discount * float(total)
		elif discount_type == 'absolute':
			discount = discount_amount
		else:
			raise ValueError("Invalid discount type")
		return discount