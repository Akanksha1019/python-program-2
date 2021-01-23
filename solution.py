
class Number:
	counter = 1

	def __init__(self, num):
		self.num = num

	@staticmethod
	def update(a):
		Number.counter += a

obj1 = Number(3)
a = int(input())
Number.update(a)
print(Number.counter)

