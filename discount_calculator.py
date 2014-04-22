
class DiscountCalculator(object):
	def calculate(self, total, discount_amount, discount_type):
		if discount_type == "percent":
			if discount_amount > 100:
				raise ValueError("Percentage discount cannot exceed 100")
			else:
				percentage_discount = float(discount_amount) / 100
				discount = percentage_discount * float(total)
		elif discount_type == 'absolute':
			if discount_amount > total:
				raise ValueError("Discount amount cannot exceed total amount")
			else:
				discount = discount_amount
		else:
			raise ValueError("Invalid discount type")
		return discount
