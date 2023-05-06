n=input("Enter the sentence=")
count=dict()
a=n.split()

for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Total words=",count)


