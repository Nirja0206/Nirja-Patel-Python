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
class D(A):
    def getD(self,d):
        self.d=d
        return self.d
    
    
b1=B()
c1=C()
d1=D()
d1.getA(int(input("Enter the value:")))
b1.getB(int(input("Enter the value:")))
c1.getC(int(input("Enter the value:")))
d1.getD(int(input("Enter the value:")))
