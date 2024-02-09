"""This file contains the object definitions and classifications for tables and seats. There are 6 tables and 4 seats at each table for a total of 24 seats."""

class Seat:
    # Class that defines the seat's status as being free or not free and then the occupant that is occupying the seat if it is not free
    
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name
            self.free = False    

class Table:
    # Class that defines the table's seat capacity and remaining available seats
    
    def __init__(self, capacity = 4):
        self.capacity = 4
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name:str):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        return self.capacity - len(self.seats)


            
