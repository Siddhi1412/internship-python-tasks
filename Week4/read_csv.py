# HANDS-ON
# 3] Make a program that reads data from CSV file

import csv

# -------------------------------------------------
# Reading data from CSV file
# -------------------------------------------------
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found!")
except Exception as e:
    print("Error:", e)
