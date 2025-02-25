print("Welcome to our Clothing Store!")
print("In our store, you can buy clothes for Men, Women, and Kids.")
print("In Men's category, you can buy:\n - Jeans\n - Shirts\n - T-shirts")
print("In Women's category, you can buy:\n - Sarees\n - Dresses\n - Cloth materials")
print("In Kids' category, you can buy:\n - Caps\n - Nightwear\n - Shirt+Pant combo")
print("If you buy at least one item from all categories, you get a special discount!")

categories = ['Mens', 'Womens', 'Kids']
selected_categories = []

total = 0
discount = 0

# Ask user which categories they want to buy from
for category in categories:
    buy_from_category = input(f"Do you want to buy from {category} wear? (yes/no): ").lower()
    if buy_from_category == "yes":
        selected_categories.append(category)

# Buying from Mens
if 'Mens' in selected_categories:
    mens = int(input("Enter how many items you want to buy in Mens wear: "))
    for b in range(mens):
        a = input("Select product (jeans/shirts/t-shirts): ").lower()
        quantity = int(input("Enter quantity: "))
        if a == "jeans":
            total += quantity * 1000
            print(f"Jeans selected: {quantity}, Total: {quantity * 1000}")
        elif a == "shirts":
            total += quantity * 900
            print(f"Shirts selected: {quantity}, Total: {quantity * 900}")
        elif a == "t-shirts":
            total += quantity * 800
            print(f"T-shirts selected: {quantity}, Total: {quantity * 800}")
        else:
            print("Invalid selection. Please select from jeans, shirts, or t-shirts.")

# Buying from Womens
if 'Womens' in selected_categories:
    womens = int(input("Enter how many items you want to buy in Womens wear: "))
    for b in range(womens):
        w = input("Select product (sarees/dresses/cloth materials): ").lower()
        quantity = int(input("Enter quantity: "))
        if w == "sarees":
            total += quantity * 1000
            print(f"Sarees selected: {quantity}, Total: {quantity * 1000}")
        elif w == "dresses":
            total += quantity * 900
            print(f"Dresses selected: {quantity}, Total: {quantity * 900}")
        elif w == "cloth materials":
            total += quantity * 800
            print(f"Cloth materials selected: {quantity}, Total: {quantity * 800}")
        else:
            print("Invalid selection. Please select from sarees, dresses, or cloth materials.")

# Buying from Kids
if 'Kids' in selected_categories:
    kids = int(input("Enter how many items you want to buy in Kids wear: "))
    for b in range(kids):
        w = input("Select product (caps/nightwear/combo): ").lower()
        quantity = int(input("Enter quantity: "))
        if w == "caps":
            total += quantity * 1000
            print(f"Caps selected: {quantity}, Total: {quantity * 1000}")
        elif w == "nightwear":
            total += quantity * 900
            print(f"Nightwear selected: {quantity}, Total: {quantity * 900}")
        elif w == "combo":
            total += quantity * 800
            print(f"Shirt+Pant combo selected: {quantity}, Total: {quantity * 800}")
        else:
            print("Invalid selection. Please select from caps, nightwear, or combo.")

# Calculate discount if user bought from all three categories
if len(selected_categories) == 3:
    if total <= 5000:
        discount = total * 0.05
        print(f"You got a 5% discount for purchasing from all categories!")
    elif total <= 7500:
        discount = total * 0.10
        print(f"You got a 10% discount for purchasing from all categories!")
    elif total < 10000:
        discount = total * 0.15
        print(f"You got a 15% discount for purchasing from all categories!")
    elif total > 10000:
        discount = total * 0.20
        print(f"You got a 20% discount for purchasing from all categories!")
else:
    print("You did not buy from all categories, so no special discount.")

# Final calculation
after_discount = total - discount
print(f"Total bill after discount: {after_discount}")