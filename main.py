from table import Seat
from table import Table

filename = "./new_colleagues.csv"
seating_assignments = []

with open(filename, newline='') as list_of_colleagues:
    reader = csv.reader(list_of_colleagues)
    # Flatten the nested list using list comprehension
    seating_assignments = [name for row in reader for name in row]
    room = []
    for name in seating_assignments:
        some_seat = Seat(True, ' ')
        some_seat.set_occupant(name)
        room.append(some_seat)