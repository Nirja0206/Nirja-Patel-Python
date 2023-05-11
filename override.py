class A:
    def show(self):
        print("This is a Form of A")
class B(A):
    def show(self):
        super().show()
        print("This is a Form of B")
class C(A):
    def show (self):
        super().show()
        print("This is a Form of C")
class D(B,C):
    def show(self):
        super().show()
        print("This is a Form of D")
d1=D()
d1.show()
