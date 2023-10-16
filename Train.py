from Cabin import Cabin

class Train:
    def __init__(self, train_no, no_of_cabins):
        self.train_no = train_no
        self.no_of_cabins = no_of_cabins
    
    def build(self):
        self.cabins = []
        for i in range(self.no_of_cabins):
            self.cabins.append(
                Cabin(
                    cabin_num=i+1,
                    total_seats=9
                ).build()
            )
        return self

    def get_available_seats(self):
        seats = 0
        for cabin in self.cabins:
            seats += cabin.get_available_seats()
        return seats

    def get_available_pref_seats(self, pref):
        seats = 0
        for cabin in self.cabins:
            seats += cabin.get_available_pref_seats(pref)
        return seats

    def allot_seat(self, passenger, pref):
        if pref:
            for cabin in self.cabins:
                for seat in cabin.seats:
                    if seat.position == passenger.seat_preference and seat.status == "Available":
                        seat.status = "Booked"
                        cabin.available_seats -= 1
                        cabin.booked_seats += 1
                        return (cabin.cabin_num, seat.seat_num, seat.position)
        else:
            for cabin in self.cabins:
                for seat in cabin.seats:
                    if seat.status == "Available":
                        seat.status = "Booked"
                        cabin.available_seats -= 1
                        cabin.booked_seats += 1
                        return (cabin.cabin_num, seat.seat_num, seat.position)
