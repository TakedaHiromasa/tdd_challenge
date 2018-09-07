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

	def testInput(self):
		self.assertEqual(self.input_list.input_list(), [[10, 12], [40, 16], [100, 45], [], [50, 50, 55]])

class OutputTest(unittest.TestCase):
	def setUp(self):
		self.output_list = Output_list(io.StringIO(""""""))