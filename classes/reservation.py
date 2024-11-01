class Reservation:
    """Represents a reservation with passenger, flight details, and status."""
    
    def __init__(self, reservation_id, passenger, flight):
        """
        Initializes a reservation with the given ID, passenger, and flight.
        
        Args:
            reservation_id (str): Unique identifier for the reservation.
            passenger (Passenger): Passenger object associated with the reservation.
            flight (Flight): Flight object associated with the reservation.
        """
        self.reservation_id = reservation_id
        self.passenger = passenger
        self.flight = flight
        self.status = "booked"  # Default status

    def make_reservation(self):
        """Books a reservation and confirms the status."""
        self.status = "booked"
        print(f"Reservation {self.reservation_id} for {self.passenger.name} is booked.")

    def cancel_reservation(self):
        """Cancels the reservation and updates the status."""
        self.status = "canceled"
        print(f"Reservation {self.reservation_id} has been canceled.")

    def view_reservation(self):
        """Displays the reservation details."""
        details = (
            f"Reservation ID: {self.reservation_id}\n"
            f"Passenger: {self.passenger.get_details()}\n"
            f"Flight Number: {self.flight.flight_number}\n"
            f"Status: {self.status}"
        )
        print(details)
