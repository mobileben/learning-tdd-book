from money import Money
import functools
import operator

class Portfolio:
	def __init__(self):
		self.moneys = []
		self._eurToUsd = 1.2

	def __convert(self, aMoney, aCurrency):
		eurToUsd = 1.2
		if aMoney.currency == aCurrency:
			return aMoney.amount
		else:
			return aMoney.amount * self._eurToUsd

	def add(self, *money):
		self.moneys.extend(money)

	def evaluate(self, currency):
		total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0)
		return Money(total, currency)


