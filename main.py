import csv
from utils.openspace import Openspace

# Load colleagues from CSV file
colleagues = []
with open("new_colleagues.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        colleagues.extend(row)

# Create Openspace instance with 3 tables
openspace = Openspace(6)

# Organize colleagues into seats
openspace.organize(colleagues)

# Display the results
openspace.display()

# Store the results in an excel file
openspace.store("assigned_seats.xlsx")