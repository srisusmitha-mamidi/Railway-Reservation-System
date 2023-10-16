from Train import Train
from Passenger import Passenger
from User import User
from Bookings import Bookings 

def main():
    train = Train(train_no=12181, no_of_cabins=2).build()
    bookings = Bookings()

    passenger1 = Passenger()
    passenger1.set_seat_preference("Lower").set_name("Saurabh").set_age(28)
    passenger2 = Passenger()
    passenger2.set_seat_preference("Middle").set_name("Akhil").set_age(45)
    passenger3 = Passenger()
    passenger3.set_seat_preference("Upper").set_name("Aman").set_age(85)
    passenger4 = Passenger()
    passenger4.set_seat_preference("Middle").set_name("Ajay").set_age(4)

    user1 = User("Vijay")
    user1.add_passenger(passenger2)
    user1.add_passenger(passenger3)
    user1.add_passenger(passenger4)
    ticket = user1.book_seats(train)
    bookings.add_booking(ticket)
    print(ticket)

    user1.add_passenger(passenger1)
    ticket = user1.book_seats(train)
    bookings.add_booking(ticket)
    print(ticket)

    ticket = user1.book_seats(train)
    bookings.add_booking(ticket)
    print(ticket)

    user2 = User("Ramesh")
    user2.add_passenger(passenger2)
    ticket = user2.book_seats(train)
    bookings.add_booking(ticket)
    print(ticket)

    ticket = user1.book_seats(train)
    bookings.add_booking(ticket)
    print(ticket)

    try:
        ticket = user1.book_seats(train)
        bookings.add_booking(ticket)
        print(ticket)
    except Exception as exc:
        print(exc)

    bookings.show_bookings()

if __name__ == '__main__':
    main()
