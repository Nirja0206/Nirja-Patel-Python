import random
l=[]
lucky=[]
for i in range(1,100):
    l.append(i)

for i in range(11):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
    
print(l)
print(lucky)
    
