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
        self.tables = [Table() for _ in range(number_of_tables)]

    def organize(self, names):
        """
        Assigns colleagues to available seats randomly across the tables.

        Args:
            names (list): A list of colleague names to be assigned to seats.
        """
        random.shuffle(names)
        current_table_index = 0
        for name in names:
            while current_table_index < len(self.tables):
                if self.tables[current_table_index].has_free_spot():
                    self.tables[current_table_index].assign_seat(name)
                    break
                current_table_index += 1
            if current_table_index == len(self.tables):
                current_table_index = 0

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
