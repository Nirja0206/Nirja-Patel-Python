class A:
    def __init__(self,x,y):
        print("it is init method")
        self.x=x
        self.y=y
        print(x,y)
    def __str__(self):
        print("It is str Method")
        return"({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        x=self.x+obj.x
        y=self.y+obj.y
        return A(x,y)

a=A(10,20)
print(a)
a1=A(30,40)
print(a1)
print("Addition of 2 object:",a+a1)
