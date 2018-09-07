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

	def calc_print(self):
		result_list = []
		result_list.append(self.calc_price([10, 12]))
		result_list.append(self.calc_price([40, 16]))
		result_list.append(self.calc_price([100, 45]))
		result_list.append(self.calc_price([50, 50, 55]))
		result_list.append(self.calc_price([1000]))
		result_list.append(self.calc_price([20, 40]))
		result_list.append(self.calc_price([30, 60, 90]))
		result_list.append(self.calc_price([11, 12, 13]))
		for result in result_list:
			print(result)


if __name__ == '__main__':
	calc_price = Calc_price()
	calc_price.calc_print()
