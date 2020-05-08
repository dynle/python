class C(object):
	def __init__(self, v1, v2):
		if isinstance(v1, int):
			self.v1 = v1
		if isinstance(v2, int):
			self.v2 = v2
	def add(self):
		return self.v1 + self.v2
	def subtract(self):
		return self.v1 - self.v2
	def setV1(self, v1):
		if isinstance(v1, int):
			self.v1 = v1
	def getV1(self):
		return self.v1

c1 = C(10, 10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
print(c1.getV1())
print(c1.add())
