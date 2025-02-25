#Grocery store 

# Function to calculate the total price of each item
def calculate_total_price(weight_in_kg, price_per_kg):
    total_price = weight_in_kg * price_per_kg
    return total_price

# Main function to input and display grocery items
def main():
    grocery_list = []
    number_of_items = int(input("Enter the number of grocery items: "))
    
    # Input grocery item details
    for i in range(number_of_items):
        print(f"\nEnter details for item {i+1}:")
        item_name = input("Enter item name: ")
        weight_in_kg = float(input(f"Enter weight in kg for {item_name}: "))
        price_per_kg = float(input(f"Enter price per kg for {item_name}: "))
        
        # Calculate total price using the defined function
        total_price = calculate_total_price(weight_in_kg, price_per_kg)
        
        # Store item details in the list
        grocery_list.append({
            "item": item_name,
            "weight": weight_in_kg,
            "price_per_kg": price_per_kg,
            "total_price": total_price
        })
    
    # Print grocery items and total prices
    print("\nGrocery List:")
    for item in grocery_list:
        print(f"{item['item']} - {item['weight']} kg @ {item['price_per_kg']} per kg. Total: {item['total_price']}")
    
if __name__ == "__main__":
    main()




















