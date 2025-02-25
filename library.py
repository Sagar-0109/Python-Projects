class user:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.cart=[]


    def add_to_cart(self,book):
        self.cart.append(book)
        print(f" {book.title} book has been added to your cart")


    def view_cart(self):
        if not self.cart:
            print("Your cart is empty")

        else:
            print("Your books in cart")
            total_price=0
            for book in self.cart:
                print(f"Title: {book.title} by {book.author} Price: ${book.price:.2f}")
                total_price+=book.price
                print(f"Total price: ${total_price:.2f}")


    def checkout(self):
        if not self.cart:
            print("Your cart is empty.Add books to your cart to check out")
            return
        total_price = sum(books.price for books in self.cart)
        print(f"Your total price is ${total_price:.2f}")
        payment = input("Proceed to payment? (yes/no): ")
        if payment.lower() == 'yes':
            print("Payment processed successfully. Thank you for your purchase!")
            self.cart.clear()  # Clear the cart after successful payment
        else:
            print("Payment cancelled.")

    
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def register_user(self, username, password):
        if username in self.users:
            print("User  already exists! Please choose a different username.")
            return False
        else:
            self.users[username] = user(username, password)
            print(f"User  '{username}' registered successfully.")
            return True

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid username or password!")
            return None

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book.title} by {book.author} - ${book.price:.2f}")


def main():
    library = Library()

    # Adding some books to the library with prices
    library.add_book(Book("1984", "George Orwell", 9.99))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 7.99))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", 8.99))
    library.add_book(Book("The Catcher in the Rye", "J.D. Salinger",10.89))
    library.add_book(Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams",15.8))
    library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien",12.99))
    library.add_book(Book("The Picture of Dorian Gray", "Oscar Wilde", 11))
    library.add_book(Book("The Adventures of Huckleberry Finn", "Mark Twain",125))
    library.add_book(Book("The Count of Monte Cristo", "Alexandre Dumas",10.5))
    library.add_book(Book("The Scarlet Letter", "Nathaniel Hawthorne", 9.7))
    library.add_book(Book("The War of the Worlds", "H.G. Wells", 8.87))

  



    # User registration
    num_users = int(input("How many users do you want to register? "))
    for _ in range(num_users):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if library.register_user(username, password):
                break  # Exit loop if registration is successful

    # User login
    username = input("Enter your username to log in: ")
    password = input("Enter your password: ")

    user = library.login(username, password)

    if user:
        while True:
            print("\n1. View available books")
            print("2. Add book to cart")
            print("3. View cart")
            print("4. Checkout")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                library.display_books()
            elif choice == "2":
                book_title = input("Enter the title of the book to add to cart: ")
                # Find the book in the library
                book = next((b for b in library.books if b.title.lower() == book_title.lower()), None)
                if book:
                    user.add_to_cart(book)
                else:
                    print("Book not found!")
            elif choice == "3":
                user.view_cart()
            elif choice == "4":
                user.checkout()
            elif choice == "5":
                print("Thank you for visiting our library hope to see you soon")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
        


