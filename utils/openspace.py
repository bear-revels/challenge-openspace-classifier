"""This file contains the object definitions and classifications for openspaces in the office. There are 6 tables and 4 seats at each table for a total of 24 seats."""

#import libraries and classes
import random
import pandas as pd
from .table import Table

class Openspace:
    """
    Class that defines the number of tables and seats within the workspace.
    """

    def __init__(self, number_of_tables:int):
        """
        Initializes an Openspace object with the specified number of tables.

        Args:
            number_of_tables (int): The number of tables in the openspace.
        """
        self.number_of_tables = number_of_tables
        self.tables = [Table() for _ in range(number_of_tables)] # list containing 'number_of_tables' instances of the 'Table' class

    def organize(self, names):
        random.shuffle(names) #shuffle the list of names
        for table in self.tables:
            while table.has_free_spot() and names: # if there is a free seat at the table and a name on the list
                name_of_colleague = names.pop() # remove a name from the list
                table.assign_seat(name_of_colleague) # add that name to the seat
        if len(names) != 0:
            for x in names:
                print(f'{x} dose not have a seat available')

    def display(self):
        """
        Displays the assigned seats for each table.
        """
        for i, table in enumerate(self.tables):
            print(f'Table {i+1}:')
            for j, seat in enumerate(table.seats):
                print(f"Seat {j+1}: {'Empty' if seat.free else seat.occupant}")

    def store(self, filename):
        """
        Stores the assigned seats in an Excel file.

        Args:
            filename (str): The filename for the Excel file.
        """
        data = []
        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                data.append([f"Table {i}", f"Seat {j}", seat.occupant if not seat.free else "Empty"])
        df = pd.DataFrame(data, columns=["Table", "Seat", "Occupant"])
        df.to_excel(filename, index=False)