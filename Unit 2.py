class BankAccount:
    def __init__(self, account_num, balance=0):
        self.account_num = account_num
        self.balance = balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print("deposited amount is :",self.balance)
        else:
            print("Please enter a valid amount")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print("With dwall amount is :",self.balance)
        else:
            print("No balance")

    def check_balance(self):
        print("Current balance: ",self.balance)
        return self.balance 
if __name__=="__main__":
    account=BankAccount("281207",1000)
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            account.check_balance()
        elif choice=="2":
            amount=float(input("Enter amount to deposit"))
            account.deposit(amount)
        elif choice=="3":
            amount=float(input("Enter amount of withdrawl"))
            account.withdraw(amount)
        elif choice=="4":
            print("Have a nice Day :)")
            break
        else:
            print("Invalid choice")




