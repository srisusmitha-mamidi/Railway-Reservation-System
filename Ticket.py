import random

class Ticket:
    def __init__(self, train_no):
        self.pnr_num = random.randint(1111111111, 9999999999)
        self.train_no = train_no
        self.ticket_metadata = {
            "passenger": [],
            "cabin_num": [],
            "seat_num": [],
            "position": [],
            "status": []
        }
    
    def add_reserved_passenger(self, passenger, cabin_num, seat_num, position, status):
        self.ticket_metadata["passenger"].append(passenger)
        self.ticket_metadata["cabin_num"].append(cabin_num)
        self.ticket_metadata["seat_num"].append(seat_num)
        self.ticket_metadata["position"].append(position)
        self.ticket_metadata["status"].append(status)

    def __str__(self):
        print(f"PNR - {self.pnr_num} Train No. {self.train_no}")
        for i in range(len(self.ticket_metadata["passenger"])):
            print(f'{self.ticket_metadata["passenger"][i]}')
            print(f'{self.ticket_metadata["status"][i]} - {self.ticket_metadata["cabin_num"][i]}/{self.ticket_metadata["seat_num"][i]}/{self.ticket_metadata["position"][i]}')
        return ''
