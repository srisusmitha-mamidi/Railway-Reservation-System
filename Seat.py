class Seat:
    def __init__(self, seat_num, position):
        self.seat_num = seat_num
        self.position = position
        self.status = "Available"

    def is_available(self):
        return True if self.status == "Available" else False
