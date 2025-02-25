class MetroTrainTicket:
    def __init__(self):
        # Define metro stations and corresponding distances from the starting point (in km)
        self.stations = {
            "Miyapur": 0,
            "Nizampet": 2,
            "KPHB": 5,
            "Kukatpally": 7,
            "Ameerpet": 12,
        }
        self.base_fare = 10  
        self.rate_per_km = 2

    def calculate_fare(self, start, destination):
        
        distance = abs(self.stations[destination] - self.stations[start])

        
        if distance <= 2:
            return self.base_fare
        else:
            extra_distance = distance 
            fare = self.base_fare + (extra_distance * self.rate_per_km)
            return fare

    def print_ticket(self, start, destination):
        fare = self.calculate_fare(start, destination)
        print("\n--- Metro Train Ticket ---")
        print(f"From: {start}")
        print(f"To: {destination}")
        print(f"Fare: ₹{fare}")
        print("-------------------------")

    def run(self):
        print("Welcome to Metro Train Ticketing System!")
        print("Available Stations:")
        for station in self.stations.keys():
            print(station)

    
        start = input("\nEnter the start station: ").strip()
        destination = input("Enter the destination station: ").strip()

        if start not in self.stations or destination not in self.stations:
            print("Invalid station. Please try again.")
            return

        # Print the ticket
        self.print_ticket(start, destination)



metro_ticket_system = MetroTrainTicket()
metro_ticket_system.run()