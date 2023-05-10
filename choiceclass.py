class Bank:
    #print("Open Acoount:")
    

        def open(self,accno,cname,balance):
            self.accno=accno
            self.cname=cname
            self.balance=balance
            print("your account is successfully opened with",self.balance,"balance")

        def deposite(self,amount):
            self.balance=self.balance+amount
            print("your amount is successfully deposited")

        def withdraw(self,amount):
            if(self.balance<=amount):
                self.balance=self.balance-amount
                print("your account  have insuffiecient balance ")
            else:
                print("Amount has been succesfully deducted")

        def checkbalance(self):
            print("Your Current  balnce is:",self.balance)
b=Bank()              
while(True):
        print("1.Open account")
        print("2.Deposit:")
        print("3.WithDraw:")
        print("4. Check Balance:")
        print("5. Exit")
        choice=int(input("Enter your Choice:"))
        
        if(choice==1):
            a=int(input("Enter the amount for open account:"))
            b.open(123,"Nirja",a)
        elif(choice==2):
            e=int(input("Enter the amount to deposite:"))
            b.deposite(e)
        elif(choice==3):
            c=int(input("Enter the amount ypu want to withdraw:"))
            b.withdraw(c)
        elif(choice==4):
            b.checkbalance()
        else:
            break
            
