class Flight:
    """Represents a flight with details about departure, arrival, and fare."""
    
    def __init__(self, flight_number, departure_airport, arrival_airport, 
                 departure_time, arrival_time, fare, halts, distance):
        """
        Initializes a flight with the provided details.
        
        Args:
            flight_number (str): Unique identifier for the flight.
            departure_airport (str): Departure airport code.
            arrival_airport (str): Arrival airport code.
            departure_time (str): Scheduled departure time.
            arrival_time (str): Scheduled arrival time.
            fare (float): Base fare for the flight.
            halts (list): List of halt locations.
            distance (float): Distance between departure and arrival airports.
        """
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.fare = fare
        self.halts = halts
        self.distance = distance

    def calculate_fare(self):
        """
        Calculates the flight fare based on distance and number of halts.
        
        Returns:
            float: Calculated fare.
        """
        # Fare calculation could consider distance and additional charge for halts
        halt_charge = 20 * len(self.halts)  # Adding ₹20 per halt as example
        return self.fare + (self.distance * 0.05) + halt_charge

    def is_direct(self):
        """Checks if the flight is direct (i.e., no halts)."""
        return len(self.halts) == 0
