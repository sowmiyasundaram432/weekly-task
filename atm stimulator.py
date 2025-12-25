class Account:
    def __init__(self,balance):
        self.balance=balance
    def balance_amt(self):
            with open("atm.txt","w") as file:
             file.write(f"Your balance is {self.balance}")
             print(f"Your balance is {self.balance}")
    def deposite_amt(self,amount):
        self.balance+=amount
        with open("atm.txt","a") as file:
           file.write(f"\nYour deposit is {amount}")
           print(f"Amount {amount} is deposited")
    def withdraw_amt(self,withdraw):
        if self.balance>=withdraw:
            self.balance-=withdraw
            with open("atm.txt","a") as file:
               file.write(f"\nyour withdraw amount is {withdraw}")
            print(f"Amount {withdraw} is withdrawn")
        else:
            print("Balance is not sufficient")
    def exit(self):
        with open("atm.txt","a") as file:
           file.write("\nTHANK YOU")
        print(f"Thank You"'\n'"Visit Again")

account=Account(balance=0)
while True:
    N=input("Deposite or Withdraw or Balance or Exit: ").lower()
    if N=="deposite":
        try:
         amount=int(input("Enter deposite amount:"))
        except ValueError as e:
         print(f"only number is allowed: {e}") 
        else:
         account.deposite_amt(amount)
    elif N=="withdraw":
        try:
         withdraw=int(input("Enter withdraw amount"))
        except ValueError as e:
         print(f"Only number is acceptable {e}")
        else: 
         account.withdraw_amt(withdraw)
    elif N=="balance":
        account.balance_amt()
    elif N=="exit":
        account.exit()
        break
    else:
        print("Invalid choice")