"""This file contains the object definitions and classifications for tables and seats. There are 6 tables and 4 seats at each table for a total of 24 seats."""

class Seat:
    """
    Class that defines the status of a seat and the occupant assigned to it.
    """

    def __init__(self):
        """
        Initializes a Seat object as free with no assigned occupant.
        """
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        """
        Assigns an occupant to the seat.

        Args:
            name (str): The name of the occupant.
        """
        if self.free == True:
            self.occupant = name
            self.free = False

class Table:
    """
    Class that defines a table with a specific capacity and available seats.
    """

    def __init__(self, capacity = 4):
        """
        Initializes a Table object with the specified capacity.

        Args:
            capacity (int): The maximum number of seats at the table.
        """
        self.capacity = 4
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        """
        Checks if there are any free seats at the table.

        Returns:
            bool: True if there is at least one free seat, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name:str):
        """
        Assigns a colleague to a free seat at the table.

        Args:
            name (str): The name of the colleague to be assigned.

        Returns:
            bool: True if the colleague is successfully assigned, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        """
        Calculates the remaining available seats at the table.

        Returns:
            int: The number of available seats at the table.
        """
        return self.capacity - len(self.seats)