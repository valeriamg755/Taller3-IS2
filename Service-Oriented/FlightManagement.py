
class FlightSearchService:
    def search_flights(self, origin, destination, date):
        flights = [
            {"id": 1, "origin": "NYC", "destination": "LAX", "date": "2024-05-20", "available_seats": 100},
            {"id": 2, "origin": "NYC", "destination": "SFO", "date": "2024-05-20", "available_seats": 50},
            {"id": 3, "origin": "LAX", "destination": "NYC", "date": "2024-05-22", "available_seats": 80},
        ]

        filtered_flights = [flight for flight in flights if flight["origin"] == origin and flight["destination"] == destination and flight["date"] == date]
        return filtered_flights

class SeatReservationService:
    def __init__(self):
        self.reserved_seats = set()

    def reserve_seat(self, flight_id, seat_number):
        if seat_number not in self.reserved_seats:
            self.reserved_seats.add(seat_number)
            return True
        else:
            return False

class PaymentProcessingService:
    def process_payment(self, amount, payment_details):
        print("Payment processed successfully!")
        print("Amount:", amount)
        print("Payment details:", payment_details)

class UserInterface:
    def __init__(self):
        self.flight_search_service = FlightSearchService()
        self.seat_reservation_service = SeatReservationService()
        self.payment_processing_service = PaymentProcessingService()

    def search_flights(self, origin, destination, date):
        flights = self.flight_search_service.search_flights(origin, destination, date)
        print("Available flights:")
        for flight in flights:
            print(flight)

    def reserve_seat(self, flight_id, seat_number):
        success = self.seat_reservation_service.reserve_seat(flight_id, seat_number)
        if success:
            print("Seat reserved successfully!")
            self.process_payment()
        else:
            print("Seat already reserved.")

    def process_payment(self):
        amount = 100
        payment_details = {"card_number": "1234 5678 9012 3456", "expiry_date": "05/25", "cvv": "123"}
        self.payment_processing_service.process_payment(amount, payment_details)
        print("Payment confirmation sent.")
