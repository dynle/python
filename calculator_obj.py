class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def product(self):
        return self.first * self.second

    def divide(self):
        return self.first / self.second
    
a = FourCal(4,2)
print(a.add())
print(a.product())
