from Ticket import Ticket

class User:
    def __init__(self, name):
        self.name = name
        self.passenger = []
    
    def add_passenger(self, passenger):
        self.passenger.append(passenger)

    def book_seats(self, train):
        ticket = Ticket(train.train_no)
        if train.get_available_seats() >= len(self.passenger):
            for passenger in self.passenger:
                pref = passenger.seat_preference
                if train.get_available_pref_seats(pref):
                    cabin, seat, position = train.allot_seat(passenger, pref=True)
                else:
                    cabin, seat, position = train.allot_seat(passenger, pref=False)
                ticket.add_reserved_passenger(passenger, cabin, seat, position, status="Booked")
            
            return ticket

        raise Exception("No seats are available")
