# =========================================================
# WEEK 4: FILE HANDLING & BASIC DEBUGGING TECHNIQUES
# =========================================================

# --------------------------
# SECTION 1
# --------------------------

# Writing to a file
with open("notes.txt", "w") as f:
    f.write("Hello ,this is Siddhi Learning file Handling!\n")

# Appending to a file
with open("notes.txt", "a") as f:
    f.write("I am practicing Python file handling")

# Reading the entire file
with open("notes.txt", "r") as f:
    x = f.read()
    print(x)

# .readline()- Read one single line at a time
with open("notes.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("Line 1:", line1)
    print("Line 2:", line2)

# .readlines()- Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Iterating through lines (better approach)
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())


# --------------------------
# SECTION 2: TXT & CSV FILES
# --------------------------
import csv

# Reading CSV using csv.reader()
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print("Using csv.reader():")
    for row in reader:
        print(row)

# Reading CSV using csv.DictReader()
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    print("Using csv.DictReader():")
    for row in reader:
        print(row)

# Writing to CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "age", "city"])
    writer.writerow(["Sonali", 14, "Satara"])

# Appending a single row
new_row = ["Riya", 67, "Agra"]
with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

# Appending multiple rows
rows = [
    ["priya", 13, "sdfvbn"],
    ["hello", 14, "erthj"],
    ["dmello", 98, "asdfg"]
]
with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)


# --------------------------
# SECTION 3: ERROR HANDLING FOR FILE OPERATIONS
# --------------------------

# 1. Basic Error Handling While Reading a File
try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not Found!")
except PermissionError:
    print("Error: You dont have permission to read this file")
except Exception as e:
    print("Some other error occured", e)
finally:
    print("Done trying to read the file.")

# 2. Safe Writing to a File
try:
    with open("data.txt", "w") as f:
        f.write("Hello world!")
except Exception as e:
    print("Could not write to the file:", e)

# 3. Handling Errors When Working With CSV FileExistsError
try:
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found!")
except Exception as e:
    print("Unexpected error:", e)

# Reading mydata.txt with error handling
try:
    with open("mydata.txt", "r") as f:
        x = f.read()
        print(x)
except FileNotFoundError:
    print("Text file not found")
except PermissionError:
    print("Permission not granted")
finally:
    print("Tried reading my data file")

# Try writing to a file using try/except
try:
    with open("writing.txt", "w") as f:
        f.write("This is a text file")
except Exception as e:
    print("Unexpected error:", e)

# Try reading a CSV file inside a try/except block
try:
    with open("trial.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for rows in reader:
            print(rows)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("Some other error occurred:", e)
finally:
    print("MISSION SUCCESSFULLY EXECUTED")

# --------------------------
# SECTION 5 - Basic debugging techniques
# ==============================

# 1: Age input and next year calculation
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert string to integer
next_age = age + 1

# Using str() to combine string + integer
print("Hello " + name)
print("Next year you will be " + str(next_age))

# Using comma in print (automatic conversion)
print("Hello", name)
print("Next year you will be", next_age)

# Using f-string (modern & clean)
print(f"Hello {name}")
print(f"Next year you will be {next_age}")

# 2: Adding two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2

# Using str()
print("The sum is " + str(sum_result))

# Using comma
print("The sum is", sum_result)

# Using f-string
print(f"The sum is {sum_result}")

# Notes:
# 1. input() returns string; convert to int for arithmetic
# 2. '+' with strings requires all operands to be strings
# 3. Comma in print or f-strings auto-convert numbers to string
