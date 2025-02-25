class User:
    """
    Represents a user in the system.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.booking = None  # Stores the user's booking details

    def book_room(self, hotel, room_type, hours):
        """
        Allows the user to book a room.
        """
        self.booking = hotel.book_room(self, room_type, hours)
        if self.booking:
            print(f"\nBooking successful! You booked a {room_type} room for {hours} hours.")
        else:
            print("\nBooking failed. No rooms available.")

    def make_payment(self, hotel):
        """
        Simulates the payment process and requests service rating.
        """
        if self.booking:
            print(f"\nProcessing payment for ${self.booking['total']}...")
            print("Payment successful! Enjoy your stay!")
            hotel.collect_rating()
            self.booking = None  # Reset booking after payment
        else:
            print("\nNo active booking to pay for.")


class Hotel:
    """
    Represents the hotel with room management and service rating system.
    """
    def __init__(self, name):
        self.name = name
        self.rooms = {
            "single": {"available": 5, "rate": 125},  # 5 single rooms, $125/hour
            "double": {"available": 3, "rate": 250},  # 3 double rooms, $250/hour
            "suite": {"available": 2, "rate": 500},  # 2 suites, $500/hour
        }
        self.ratings = []  # List to store service ratings

    def book_room(self, user, room_type, hours):
        """
        Books a room if available.
        """
        if room_type in self.rooms and self.rooms[room_type]["available"] > 0:
            self.rooms[room_type]["available"] -= 1
            total = self.rooms[room_type]["rate"] * hours
            return {"room_type": room_type, "hours": hours, "total": total}
        else:
            return None

    def collect_rating(self):
        """
        Collects a service rating from the user.
        """
        while True:
            try:
                rating = int(input("\nPlease rate our service on a scale of 1 to 10: "))
                if 1 <= rating <= 10:
                    self.ratings.append(rating)
                    print("\nThank you for your feedback!")
                    break
                else:
                    print("\nInvalid input. Please enter a number between 1 and 10.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

    def display_average_rating(self):
        """
        Displays the average rating of the hotel.
        """
        if self.ratings:
            average = sum(self.ratings) / len(self.ratings)
            print(f"\nAverage Service Rating for {self.name}: {average:.2f}/10")
        else:
            print("\nNo ratings available yet.")


class BookingSystem:
    """
    Manages user registration, login, and interactions with the hotel.
    """
    def __init__(self):
        self.users = {}
        self.hotel = Hotel("Grand Vistara Hotel")

    def register(self, username, password):
        """
        Registers a new user.
        """
        if username in self.users:
            print("\nUsername already exists. Please choose a different username.")
        else:
            self.users[username] = User(username, password)
            print("\nRegistration successful! You can now log in.")

    def login(self, username, password):
        """
        Logs in an existing user.
        """
        user = self.users.get(username)
        if user and user.password == password:
            print(f"\nWelcome, {username}!")
            return user
        else:
            print("\nInvalid credentials. Please try again.")
            return None


# Main Program
if __name__ == "__main__":
    system = BookingSystem()

    while True:
        print("\n--- Hotel Booking System ---")
        print("1. Register")
        print("2. Login")
        print("3. Display Average Rating")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            system.register(username, password)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = system.login(username, password)

            if user:
                while True:
                    print("\n--- Welcome to the Grand Vistara Hotel ---")
                    print("1. Book a Room")
                    print("2. Make Payment")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        print("\nAvailable Rooms:")
                        for room, details in system.hotel.rooms.items():
                            print(f"{room.capitalize()} - ${details['rate']}/hour - {details['available']} available")

                        room_type = input("Enter room type (single/double/suite): ").lower()
                        hours = int(input("Enter number of hours: "))
                        user.book_room(system.hotel, room_type, hours)

                    elif user_choice == "2":
                        user.make_payment(system.hotel)

                    elif user_choice == "3":
                        print("\nLogged out successfully.")
                        break
                    else:
                        print("\nInvalid choice. Please try again.")

        elif choice == "3":
            system.hotel.display_average_rating()

        elif choice == "4":
            print("\nThank you for Choosing Hotel Grand Vistara. See You Soon")
            break
        else:
            print("\nInvalid choice. Please try again.")