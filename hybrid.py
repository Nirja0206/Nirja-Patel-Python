class A:
    def getA(self,a):
        self.a=a
        return self.a
class B(A):
    def getB(self,b):
        self.b=b
        return self.b
class C(A):
    def getC(self,c):
        self.c=c
        return self.c
class D(B,C):
    def getD(self,d):
        self.d=d
        return self.d
    def sum(self):
        print("Sum :",self.a+self.b+self.c+self.d)

d1=D()
d1.getA(int(input("Enter the value:")))
d1.getB(int(input("Enter the value:")))
d1.getC(int(input("Enter the value:")))
d1.getD(int(input("Enter the value:")))
d1.sum()
