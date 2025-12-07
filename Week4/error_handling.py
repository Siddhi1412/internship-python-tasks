# HANDS-ON
# 6] Practice handling file-related errors

# -------------------------------------------------
# Handle “File Not Found”
# -------------------------------------------------
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: data.txt was not found. Creating a new file...")
    with open("data.txt", "w") as file:
        file.write("New file created.\n")

# -------------------------------------------------
# Handle “Permission Denied”
# -------------------------------------------------
filename = "protected.txt"

try:
    with open(filename, "w") as file:
        file.write("Trying to write...")
    print("Write successful!")
except PermissionError:
    print("Error: You don't have permission to write to this file.")

# -------------------------------------------------
# Handle Wrong CSV Format
# -------------------------------------------------
import csv

try:
    with open("sample.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                raise ValueError("Invalid CSV format")
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
except ValueError as e:
    print("CSV format error:", e)
except Exception as e:
    print("Some other error occurred:", e)

# -------------------------------------------------
# Handle Empty Files
# -------------------------------------------------
try:
    with open("empty.txt", "r") as file:
        data = file.read()
        if not data.strip():
            print("The file is empty.")
        else:
            print(data)
except FileNotFoundError:
    print("File does not exist.")

# -------------------------------------------------
# Safe Writing (Avoid Data Loss)
# -------------------------------------------------
data = "Important data"

try:
    with open("output.txt", "w") as file:
        file.write(data)
    print("Write successful")
except Exception as e:
    print("Error while writing:", e)
