from Seat import Seat

class Cabin:
    def __init__(self, cabin_num, total_seats):
        self.cabin_num = cabin_num
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.booked_seats = 0
    
    def build(self):
        n = self.total_seats//3
        self.seats = []
        k = 1
        for i in range(n):
            self.seats.append(
                Seat(
                    seat_num=k,
                    position="Lower"
                )
            )
            k += 1
            self.seats.append(
                Seat(
                    seat_num=k,
                    position="Middle"
                )
            )
            k += 1
            self.seats.append(
                Seat(
                    seat_num=k,
                    position="Upper"
                )
            )
            k += 1
        return self

    def get_available_seats(self):
        return self.available_seats

    def get_available_pref_seats(self, pref):
        seats = 0
        for seat in self.seats:
            if seat.position == pref and seat.status == "Available":
                seats += 1
        return seats
