class Calc_price:
	def __init__(self):
		pass

	def calc_price(self, price_list):
		round = lambda x: (x * 2 + 1) // 2
		sum = 0
		for price in price_list:
			sum = sum + price
		result = sum * 1.10
		result = round(result)
		result = int(result)
		return result

	def calc_print(self, input_list):
		for calc_list in input_list:
			calc_price(calc_list)

if __name__ == '__main__':
	calc_price = Calc_price()
	calc_price.calc_print()
