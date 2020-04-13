#bank apllication
import sys
class customer:
    bankname="ngr's bank"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('After deposit the balance:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds")
            sys.exit()
        else:
            self.balance=self.balance-amt
            print("The remaining balance:",self.balance)

print("Welcome to",customer.bankname)
name=input("enter ur name:")
c=customer(name)
while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option=input("Choose ur option:")
    if option=='d' or option=='D':
        amt=float(input("Enter th amount to deposit:"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter the amount to withdraw:"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Enter valid option")
