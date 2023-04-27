s=input("Enter a String=")
space=0
digit=0
alpha=0
special=0
for i in s:
        if(i.isalpha()):
            alpha+=1
        elif(i.isdigit()):
            digit+=1
        elif(i.isspace()):
            space+=1
        else:
            special+=1
print("total aplhabets:",alpha)
print("total digit:",digit)
print("total  space:",space)
print("total special character:",special)
