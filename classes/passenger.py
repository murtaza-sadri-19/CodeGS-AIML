class Passenger:
    """Represents a passenger with personal information."""
    
    def __init__(self, name, age, contact):
        """
        Initializes a passenger with the provided details.
        
        Args:
            name (str): Passenger's full name.
            age (int): Passenger's age.
            contact (str): Contact information (e.g., phone or email).
        """
        self.name = name
        self.age = age
        self.contact = contact

    def get_details(self):
        """Prints the passenger's details."""
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact}"
