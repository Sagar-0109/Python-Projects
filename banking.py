import random as ran
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}"
        else:
            return "Insufficient balance or invalid amount."

    def check_balance(self):
        return f"Account Balance: ₹{self.balance}"

    def display_account_details(self):
        return (f"\n--- Account Details ---\n"
                f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ₹{self.balance}\n")

    print("Welcome to the Bank!")
    

    
x = input("Enter account number (10 digits): ")


        
if len(x) == 10 and x.isdigit():  
                y = str(input("Enter user name: "))
                a=ran.randint(10000,100000)
                account = BankAccount(account_number=x, account_holder=y, balance=a)
                
                
                print(account.display_account_details())
                print("1)deposit")
                print("2)withdraw")
                print("3)check balance")
                print("4)exit")

                select=int(input("enter the code "))
                
                if select==1:
                    deposit_amount = int(input("Enter amount to deposit: "))
                    print(account.deposit(deposit_amount))

                elif select==2:
                    withdraw_amount = int(input("Enter amount to withdraw: "))
                    print(account.withdraw(withdraw_amount))

                elif select==3:
                    print(account.check_balance())
                elif select==4:
                    print("thank you for visiting")

                

else:
    print("Invalid account number. It must be exactly 10 digits long and numeric.")

