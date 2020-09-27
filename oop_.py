class Cal(object):
    def __init__(self,v1,v2):
        self.v1 = v1 #if put __ in front of the variable,
        self.v2 = v2 #cannot access to the variable outside of the Class

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return abs(self.v1-self.v2)

    def getV1(self):
        return self.v1
        
    def setV1(self,v):
        if isinstance(v, int):
            self.v1 = v 
        else:
            print("error")

c1 = Cal(10,10)
#c1.v1 = 10 : possible to access to the variable outside of the Class in python 
print(c1.getV1()) #but use set/get method 
c1.setV1("one")
print(c1.getV1())
# print(c1.add())
# print(c1.subtract())

# c2 = Cal(10,30)
# print(c2.add())
# print(c2.subtract())
