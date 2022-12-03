from money import Money
import functools
import operator

class Portfolio:
	def __init__(self):
		self.moneys = []

	def add(self, *money):
		self.moneys.extend(money)

	def evaluate(self, bank, currency):
		total = 0.0
		failures = []
		for m in self.moneys:
			try:
				total += bank.convert(m, currency).amount
			except Exception as ex:
				failures.append(ex)

		if len(failures) == 0:
			return Money(total, currency)
		failureMessage = ",".join(f.args[0] for f in failures)
		raise Exception("Missing exchange rate(s):[" + failureMessage + "]")


