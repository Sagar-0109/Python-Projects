class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def total_cost(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def display_cart(self):
        print("\nShopping Cart:")
        for item_name, details in self.items.items():
            product = details['product']
            quantity = details['quantity']
            print(f"{product.name} - ${product.price} x {quantity} = ${product.price * quantity}")
        print(f"Total Cost: ${self.total_cost()}")

def main():
    categories = {
        'Clothing': [Product('T-shirt', 20), Product('Jeans', 40)],
        'Footwear': [Product('Sneakers', 60), Product('Sandals', 30)],
        'Accessories': [Product('Watch', 100), Product('Hat', 15)]
    }

    cart = ShoppingCart()

    print("Welcome to the Fashion Store!")
    
    while True:
        print("\nSelect a category:")
        for idx, category in enumerate(categories.keys(), start=1):
            print(f"{idx}. {category}")
        print("0. Checkout")

        category_choice = int(input("Enter the category number (0 to checkout): "))
        
        if category_choice == 0:
            break
        
        category_name = list(categories.keys())[category_choice - 1]
        products = categories[category_name]

        print(f"\nAvailable products in {category_name}:")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product.name} - ${product.price}")

        while True:
            product_choice = int(input("Select a product number (0 to go back): "))
            
            if product_choice == 0:
                break
            
            selected_product = products[product_choice - 1]
            quantity = int(input(f"Enter quantity for {selected_product.name}: "))
            cart.add_item(selected_product, quantity)

    cart.display_cart()

if __name__ == "__main__":
    main()

    