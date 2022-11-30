from money import Money
from portfolio import Portfolio

import unittest

class TestMoney(unittest.TestCase):
	def testAddition(self):
		fiveDollars = Money(5, "USD")
		tenDollars = Money(10, "USD")
		fifteenDollars = Money(15, "USD")
		portfolio = Portfolio()
		portfolio.add(fiveDollars, tenDollars)
		self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

	def testMultiplication(self):
		tenEuros = Money(10, "EUR")
		twentyEuros = Money(20, "EUR")
		self.assertEqual(twentyEuros, tenEuros.times(2))

	def testDivision(self):
		originalMoney = Money(4002, "KRW")
		expectedMoneyAfterDivision = Money(1000.5, "KRW")
		self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

if __name__ == '__main__':
	unittest.main()
