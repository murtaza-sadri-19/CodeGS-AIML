class Airline:
    """Represents an airline with its basic information and flights."""
    
    def __init__(self, name, code, headquarters):
        """
        Initializes an airline with the provided name, code, and headquarters.
        
        Args:
            name (str): Name of the airline.
            code (str): Unique code for the airline.
            headquarters (str): Location of the airline's headquarters.
        """
        self.name = name
        self.code = code
        self.headquarters = headquarters
        self.flights = []

    def add_flight(self, flight):
        """
        Adds a flight to the airline's list of flights.
        
        Args:
            flight (Flight): A Flight object to add.
        """
        self.flights.append(flight)

    def get_flights(self):
        """Returns a list of all flights associated with this airline."""
        return self.flights
