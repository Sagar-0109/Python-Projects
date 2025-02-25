#ATM process

class ATM:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []

    def authenticate(self, username, password):
        """Authenticate the user"""
        return username == self.username and password == self.password

    def check_past_balance(self):
        """Check the past balance"""
        print(f"Your past balance is: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw cash from the account"""
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            print(f"Withdrew: ${amount:.2f}")
            print(f"Remaining balance: ${self.balance:.2f}")
            self.mini_statement()  

    def deposit(self, amount):
        """Deposit cash into the account"""
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount:.2f}")
        print(f"Deposited: ${amount:.2f}")
        print(f"New balance: ${self.balance:.2f}")
        self.mini_statement()  

    def mini_statement(self):
        """Display the last 5 transactions"""
        if not self.transactions:
            print("No transactions available.")
        else:
            print("Mini Statement:")
            for i, transaction in enumerate(self.transactions[-5:], start=1):
                print(f"{i}. {transaction}")

    def check_balance(self):
        """Check the current balance"""
        print(f"Your current balance is: ${self.balance:.2f}")

    def exit(self):
        """Exit the ATM system"""
        print("Thank you for using our ATM. Hope We See you soon")


def main():
    atm = ATM("Sagar", "Sagar@1980", 10000)

    print("Welcome to our ATM!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if atm.authenticate(username, password):
        print("Login successful!")
        while True:
            print("\nATM Menu:")
            print("1. Check Past Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Mini Statement")
            print("5. Check Balance")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                atm.check_past_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            elif choice == "4":
                atm.mini_statement()
            elif choice == "5":
                atm.check_balance()
            elif choice == "6":
                atm.exit()
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Please try again.")


if __name__ == "__main__":
    main()