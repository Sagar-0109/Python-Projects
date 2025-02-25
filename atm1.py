username = "Sagar"
password = "Sagar@1980"
balance = 10000
transactions = []

def display_mini_statement():
    if not transactions:
        print("No transactions available.")
    else:
        print("Mini Statement:")
        for i, transaction in enumerate(transactions[-5:], start=1):
            print(f"{i}. {transaction}")

print("Welcome to our ATM!")
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if entered_username == username and entered_password == password:
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
            print(f"Your past balance is: ${balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                transactions.append(f"Withdrawal: -${amount:.2f}")
                print(f"Withdrew: ${amount:.2f}")
                print(f"Remaining balance: ${balance:.2f}")
                display_mini_statement()
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: $"))
            balance += amount
            transactions.append(f"Deposit: +${amount:.2f}")
            print(f"Deposited: ${amount:.2f}")
            print(f"New balance: ${balance:.2f}")
            display_mini_statement()
        elif choice == "4":
            display_mini_statement()
        elif choice == "5":
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "6":
            print("Thank you for using our ATM. Hope We See you soon")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid username or password. Please try again.")
