import random
data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,1000)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
l=data.read().split(",")[:-1:]
print(l)
data.close()

