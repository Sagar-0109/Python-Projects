def login(users):
    print("Welcome to Varma-Stores!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials, please try again.")
        return None

def select_items():
    print("\nSelect items you want to buy:")
    vegetables = ['Carrot', 'Potato', 'Tomato', 'Onion', 'Cucumber']
    fruits = ['Apple', 'Banana', 'Grapes', 'Mango', 'Orange']
    groceries = ['Rice', 'Wheat', 'Salt', 'Sugar', 'Tea']

    print("Vegetables:", vegetables)
    print("Fruits:", fruits)
    print("Groceries:", groceries)

    selected_items = []
    while True:
        item = input("\nEnter item name to add to your cart (or type 'done' to finish): ")
        if item == 'done':
            break
        elif item in vegetables or item in fruits or item in groceries:
            selected_items.append(item)
        else:
            print("Item not available. Try again.")
    
    return selected_items

def select_packaging():
    print("\nChoose your packaging:")
    print("1. Wooden Box")
    print("2. Paper Bag")
    print("3. Plastic Bag")
    print("4. Carton Box")
    
    packaging_choice = input("\nEnter packaging option (1-4): ")
    if packaging_choice == '1':
        packaging = "Wooden Box"
    elif packaging_choice == '2':
        packaging = "Paper Bag"
    elif packaging_choice == '3':
        packaging = "Plastic Bag"
    elif packaging_choice == '4':
        packaging = "Carton Box"
    else:
        packaging = "Invalid choice"
        print("Invalid choice. Defaulting to Carton Box.")
    return packaging

def payment():
    print("\nSelect payment method:")
    print("1. UPI ID")
    print("2. Credit Card")
    
    payment_choice = input("\nEnter payment method (1-2): ")
    
    if payment_choice == '1':
        upi_ids = ['abc@upi', 'def@upi', 'ghi@upi', 'jkl@upi', 'mno@upi']
        print("\nAvailable UPI IDs:", upi_ids)
        upi = input("Enter your UPI ID: ")
        if upi in upi_ids:
            payment_method = f"UPI payment through {upi}"
        else:
            payment_method = "Invalid UPI ID"
            print("Invalid UPI ID, defaulting to Credit Card.")
            payment_method = "Credit Card"
    elif payment_choice == '2':
        credit_cards = ['1234-5678-9876-5432', '2345-6789-8765-6543', '3456-7890-7654-7654', '4567-8901-6543-8765', '5678-9012-5432-9876']
        print("\nAvailable Credit Cards:", credit_cards)
        card = input("Enter your Credit Card number: ")
        if card in credit_cards:
            payment_method = f"Credit Card payment through {card}"
        else:
            payment_method = "Invalid Credit Card"
            print("Invalid Credit Card, defaulting to UPI.")
            payment_method = "UPI"
    else:
        payment_method = "Invalid choice"
        print("Invalid choice. Defaulting to UPI.")
        payment_method = "UPI"
    
    return payment_method

def generate_bill(username, selected_items, packaging, payment_method):
    total_cost = len(selected_items) * 10  # Assume each item costs 10 units
    print("\nGenerating bill...")
    print(f"Bill for {username}")
    print("Items Purchased:", ", ".join(selected_items))
    print(f"Packaging: {packaging}")
    print(f"Payment Method: {payment_method}")
    print(f"Total Cost: {total_cost} units")
    return total_cost

def main():
    users = {'sagar@123': '1980', 'sagar@234': '1981', 'sagar@345': '1982', 'sagar@456': '1983', 'sagar@567': '1984'}
    
    while True:
        username = login(users)
        
        if username:
            selected_items = select_items()
            if selected_items:
                packaging = select_packaging()
                payment_method = payment()
                total_cost = generate_bill(username, selected_items, packaging, payment_method)
                print(f"\nYour total bill is {total_cost} units. Thank you for shopping!")
            else:
                print("No items selected. Exiting the process.")
        else:
            print("Exiting the system.")
            break

if __name__ == "__main__":
    main()