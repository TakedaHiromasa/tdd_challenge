import unittest
from calc_price import Calc_price

class CalcTest(unittest.TestCase):
	def setUp(self):
		self.calc_price = Calc_price()

  def testPrice(self):
		self.assertEqual(self.calc_price.calc_price([10, 12]), 24)
