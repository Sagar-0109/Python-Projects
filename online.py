#online shopping 
class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def apply_discount(self, discount_percentage):
        """Apply discount to the product price."""
        discount_amount = (self.price * discount_percentage) / 100
        return self.price - discount_amount

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f} - Stock: {self.stock}"


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def total_cost(self, discount_percentage=0):
        """Calculate total cost of the order, applying discount if provided."""
        if discount_percentage > 0:
            discounted_price = self.product.apply_discount(discount_percentage)
            return discounted_price * self.quantity
        return self.product.price * self.quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, product, quantity, discount_percentage=0):
        if product.stock >= quantity:
            order = Order(self, product, quantity)
            product.update_stock(quantity)
            self.orders.append(order)
            total_cost = order.total_cost(discount_percentage)
            print(f"Order placed for {quantity} x {product.name}. Total cost: ${total_cost:.2f}")
        else:
            print("Error: Not enough stock")

    def view_orders(self):
        print(f"Orders for {self.name}:")
        for order in self.orders:
            print(f"Order: {order.product.name}, Quantity: {order.quantity}, Total Cost: ${order.total_cost():.2f}")


class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(product)

    def total_sales(self):
        total = 0
        for customer in self.customers:
            for order in customer.orders:
                total += order.total_cost()
        return total


# Example Usage
store = Store()

# Adding products
store.add_product(Product("Men's T-Shirt", 19.99, "Men", 100))
store.add_product(Product("Men's shirt", 25.5, "Mens", 150))
store.add_product(Product("Men's Kurtas", 150, "Mens", 1500))
store.add_product(Product("Women's T-Shirt", 15.99, "Women", 200))
store.add_product(Product("Women's shirt", 20.5, "Women", 100))
store.add_product(Product("Kids T-Shirt", 10.99, "Kids", 150))
store.add_product(Product("Kids shirt", 12.5, "Kids", 100))
store.add_product(Product("Women's Dress", 49.99, "Women", 50))
store.add_product(Product("Children's Jacket", 29.99, "Children", 30))
store.add_product(Product("Men's Jeans", 39.99, "Men", 75))
store.add_product(Product("Women's Blouse", 24.99, "Women", 60))
store.add_product(Product("Children's Shorts", 15.99, "Children", 40))

# ... (previous code remains the same)

# User interaction to place orders
customer_name = input("Enter your name: ")
customer_email = input("Enter your email: ")
customer = Customer(customer_name, customer_email)
store.add_customer(customer)

while True:
    print("\nWelcome to the Sagar's Clothing Store!")
    store.display_products()
    
    product_name = input("Enter the product name you want to buy (or 'exit' to quit): ")
    if product_name.lower() == 'exit':
        break

    product = store.find_product(product_name)
    if product:
        quantity = int(input(f"How many {product.name} would you like to buy? "))
        discount_percentage = float(input("Enter discount percentage (if any, else enter 0): "))
        customer.place_order(product, quantity, discount_percentage)
    else:
        print("Product not found. Please try again.")

# Billing summary
print(f"\nThank you for shopping, {customer.name}!")
print("Your order summary:")
customer.view_orders()
total_spent = sum(order.total_cost() for order in customer.orders)
print(f"Total amount spent: ${total_spent:.2f}")
print("We hope to see you again soon!")