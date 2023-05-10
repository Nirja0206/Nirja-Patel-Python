try:
    a=int(input("Enter the Value:"))
    b=int(input("Enter the value:"))
    c=a/b

except Exception as e:
    print(e)
finally:
    print("completed")
