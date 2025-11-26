# ---------------------------------------
# Python Basics Practice
# Conditional statements, loops, lists, try-except
# ---------------------------------------

# -----------------------------
# Conditional statements: if, elif, else
# -----------------------------
age = int(input("Enter your age: "))

if age < 0:
    print("Enter a valid age")
elif age < 12:
    print("You're a child")
elif age < 17:
    print("You're a teenager")
elif age < 59:
    print("You're an adult")
else:
    print("You're a senior")

# -----------------------------
# Comparison operators: ==, !=, >, <, >=, <=
# -----------------------------
a = 10
b = 5

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -----------------------------
# Lists: creating, accessing, modifying
# -----------------------------
fruits = ["apple", "banana", "mango"]
print("Full list:", fruits)

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Append item
fruits.append("orange")
print("After adding:", fruits)

# Remove by name
fruits.remove("banana")
print("After removing banana:", fruits)

# Insert at a specific position
fruits.insert(1, "kiwi")
print("After inserting kiwi:", fruits)

# Remove by index
fruits.pop(2)
print("After popping index 2:", fruits)

print("Length of list:", len(fruits))

print("Looping through list:")
for fruit in fruits:
    print(" -", fruit)

# -----------------------------
# For loops: repeating actions
# -----------------------------
numbers = [10, 20, 30]

for n in numbers:
    print("Value:", n)

# Range examples
for i in range(5):
    print("Loop number:", i)

for i in range(1, 6):
    print("Loop number 1-5:", i)

# Loop with index
colors = ["red", "blue", "green"]
for index in range(len(colors)):
    print(index, "-", colors[index])

# Using enumerate
for index, color in enumerate(colors):
    print(index, "-", color)

# -----------------------------
# While loops
# -----------------------------
# Simple count
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# User input until correct
password = "abc123"
user_input = ""
while user_input != password:
    user_input = input("Enter password: ")
    if user_input != password:
        print("Incorrect, try again!")
print("Access granted!")

# Print numbers from 10 to 1
a = 10
while a >= 1:
    print("Number:", a)
    a -= 1

# Countdown from user input
start = int(input("Enter a starting number: "))
while start >= 1:
    print("Counting down:", start)
    start -= 1
print("Countdown finished!")

# Counting up
end = int(input("Enter a number to count up to: "))
i = 1
while i <= end:
    print("Counting up:", i)
    i += 1
print("Counting finished!")

# Count up or down based on start and end
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start < end:
    # Counting up
    i = start
    while i <= end:
        print(i)
        i += 1
    print("Counting up finished!")
elif start > end:
    # Counting down
    i = start
    while i >= end:
        print(i)
        i -= 1
    print("Counting down finished!")
else:
    print("Start and end are the same:", start)

# Count up/down with custom step
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step (positive number): "))

if step <= 0:
    print("Step must be a positive number!")
else:
    if start < end:
        # Counting up
        i = start
        while i <= end:
            print(i)
            i += step
        print("Counting up finished!")
    elif start > end:
        # Counting down
        i = start
        while i >= end:
            print(i)
            i -= step
        print("Counting down finished!")
    else:
        print("Start and end are the same:", start)

# -----------------------------
# Try-Except Examples
# -----------------------------
# Example 1
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Oops! That is not a valid number.")

# Example 2 - Division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# Example 3 - Input loop
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be positive!")
        else:
            print("Your age is:", age)
            break
    except ValueError:
        print("Invalid input! Please enter a number.")
