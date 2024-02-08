"""This file contains the object definitions and classifications for openspaces in the office. There are 6 tables and 4 seats at each table for a total of 24 seats."""

import random
import pandas as pd
from table import Table

class Openspace():
    """
    Class that defines the number of tables and seats within the new work place
    """
    
    def __init__(self, number_of_tables = 6):
        self.number_of_tables = 6
        self.tables = [Table() for _ in range(number_of_tables)]


    def organize(self, names):
        pass


    def display(self):
        pass

    def store(self, filename):
        pass
