class Passenger:
    def __init__(self):
        pass
    
    def set_name(self, name):
        self.name = name
        return self
    
    def set_age(self, age):
        self.age = age
        return self
    
    def set_seat_preference(self, pref):
        self.seat_preference = pref
        return self

    def __str__(self):
        return f"{self.name} - {self.age} - {self.seat_preference}"
