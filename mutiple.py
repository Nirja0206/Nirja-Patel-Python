class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)
    def sum(self):
        print("Sum :",self.a+self.b+self.c)
c1=C()
c1.getA(int(input("Enter the value:")))
c1.getB(int(input("Enter the value:")))
c1.getC(int(input("Enter the value:")))
c1.putA()
c1.putB()
c1.putC()
c1.sum()
