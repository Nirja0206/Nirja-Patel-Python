class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

b1=B()
b1.getA(int(input("Enter the value:")))
b1.getB(int(input("Enter the value:")))
b1.putA()
b1.putB()
