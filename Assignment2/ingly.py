a=input("Enter a string=")
b=len(a)
if(b<3):
    print("We canot change the content")
else:    
    if (a.endswith("ing")):
        s=a.replace("ing","ly")
        print(s)
    else:
        print(a+"ing")
    
