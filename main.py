from classes.airline import Airline
from classes.flight import Flight
from classes.passenger import Passenger
from classes.reservation import Reservation

# --- Define common functions ---

def create_airline():
    name = input("Enter Airline Name: ")
    code = input("Enter Airline Code: ")
    headquarters = input("Enter Airline Headquarters: ")
    return Airline(name, code, headquarters)

def create_passenger():
    name = input("Enter Passenger Name: ")
    age = int(input("Enter Passenger Age: "))
    contact = input("Enter Passenger Contact: ")
    return Passenger(name, age, contact)

# --- Define role-specific functions ---

# Passenger functions
def passenger_menu(airline):
    while True:
        print("\n--- Passenger Menu ---")
        print("1. View Available Flights")
        print("2. Make Reservation")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_flights(airline)
        elif choice == "2":
            make_reservation(airline)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# Airport Staff functions
def airport_staff_menu(airline):
    while True:
        print("\n--- Airport Staff Menu ---")
        print("1. View Available Flights")
        print("2. View Reservations")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_flights(airline)
        elif choice == "2":
            view_reservations(airline)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# Airline Staff functions
def airline_staff_menu(airline):
    while True:
        print("\n--- Airline Staff Menu ---")
        print("1. Add Flight")
        print("2. View Available Flights")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_flight(airline)
        elif choice == "2":
            view_flights(airline)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# --- Utility Functions for Viewing and Making Reservations ---

def add_flight(airline):
    flight_number = input("Enter Flight Number: ")
    departure_airport = input("Enter Departure Airport: ")
    arrival_airport = input("Enter Arrival Airport: ")
    departure_time = input("Enter Departure Time: ")
    arrival_time = input("Enter Arrival Time: ")
    fare = float(input("Enter Base Fare: "))
    halts = input("Enter Halts (comma-separated if multiple, leave blank for none): ").split(',')
    distance = float(input("Enter Distance of Flight: "))

    flight = Flight(
        flight_number=flight_number,
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        departure_time=departure_time,
        arrival_time=arrival_time,
        fare=fare,
        halts=[halt.strip() for halt in halts if halt.strip()],
        distance=distance
    )
    airline.add_flight(flight)
    print(f"Flight {flight_number} added to {airline.name}")

def view_flights(airline):
    flights = airline.get_flights()
    if flights:
        for flight in flights:
            direct_status = "Direct" if flight.is_direct() else "Indirect"
            print(f"Flight {flight.flight_number}: {flight.departure_airport} -> {flight.arrival_airport} ({direct_status})")
    else:
        print("No flights available.")

def make_reservation(airline):
    passenger = create_passenger()
    flights = airline.get_flights()

    if not flights:
        print("No available flights for this airline.")
        return

    print("\nAvailable Flights:")
    for idx, flight in enumerate(flights, start=1):
        print(f"{idx}. {flight.flight_number} from {flight.departure_airport} to {flight.arrival_airport}")

    flight_choice = int(input("Select a flight by number: ")) - 1
    selected_flight = flights[flight_choice]
    
    reservation_id = input("Enter Reservation ID: ")
    reservation = Reservation(reservation_id, passenger, selected_flight)
    reservation.make_reservation()
    reservation.view_reservation()

def view_reservations(airline):
    print("\n--- All Reservations ---")
    # Add logic to display all reservations made within the airline.
    # This requires the airline class to maintain a list of reservations.
    pass

# --- Main Program with Role Selection ---

def main():
    airline = create_airline()
    while True:
        print("\n--- Select User Role ---")
        print("1. Passenger")
        print("2. Airport Staff")
        print("3. Airline Staff")
        print("4. Exit")
        role_choice = input("Choose your role: ")

        if role_choice == "1":
            passenger_menu(airline)
        elif role_choice == "2":
            airport_staff_menu(airline)
        elif role_choice == "3":
            airline_staff_menu(airline)
        elif role_choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
