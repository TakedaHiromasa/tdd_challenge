import unittest
from input_list import Input_list
from calc_price import Calc_price
import io
import os


class InputTest(unittest.TestCase):
	def setUp(self):
		self.input_list = Input_list(io.StringIO("""10,12
40,16
100,45

50,50,55"""))
		self.calc_price = Calc_price()

	# def testPrice(self):
	# 	self.assertEqual(self.calc_price.calc_price([10, 12]), 24)
	# 	self.assertEqual(self.calc_price.calc_price([40, 16]), 62)
	# 	self.assertEqual(self.calc_price.calc_price([100, 45]), 160)
	# 	self.assertEqual(self.calc_price.calc_price([50, 50, 55]), 171)
	# 	self.assertEqual(self.calc_price.calc_price([]), 0)
	# 	self.assertEqual(self.calc_price.calc_price([40, 15]), 61)

	def testInput(self):
		self.assertEqual(self.input_list.input_list(), [[10, 12], [40, 16], [100, 45], [], [50, 50, 55]])