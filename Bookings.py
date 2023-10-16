class Bookings:
    def __init__(self):
        self.tickets = []
    
    def add_booking(self, ticket):
        self.tickets.append(ticket)

    def show_bookings(self):
        print('-'*61)
        print(f'| {"S.No.".rjust(6)} | {"Train No.".rjust(10)} | {"PNR".rjust(12)} | {"No. of Passengers".rjust(20)} |')
        print('-'*61)
        for i in range(len(self.tickets)):
            print(f'| {str(i+1).ljust(6)} | {str(self.tickets[i].train_no).rjust(10)} | {str(self.tickets[i].pnr_num).rjust(12)} | {str(len(self.tickets[i].ticket_metadata["passenger"])).rjust(20)} |')
        print('-'*61)

