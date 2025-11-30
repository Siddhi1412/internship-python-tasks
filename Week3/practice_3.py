# ==============================================================
# 1️. FUNCTIONS: Creating Reusable Code Blocks
# ==============================================================

# ----- Basic Functions -----
def welcome_message():
    print("Welcome to Python Functions!")

welcome_message()

def greet_user(name):
    print(f"Hello {name}! Welcome")

greet_user("John")

def calculate(a,b):
    print("Sum" , a+b)
    print("Difference", a-b)
    print("Product", a * b)

calculate(40,20)

# ----- Functions with Return Values -----
def square(num):
    return num * num

result = square(7)
print(result)

def power(num,exponent=2):
    return(num ** exponent)

print(power(5))
print(power(5,3))

# ==============================================================
# 2️. FUNCTION PARAMETERS AND RETURN VALUES
# ==============================================================

# ----- Function with Multiple Parameters -----
def student_info(name, age, course):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My course is {course}")

student_info(age=23,course="AI",name="John")

# ----- Variable Length Arguments -----
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(2, 3, 5))   
print(add_numbers(1, 2))      

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  
print(multiply(5, 5))    

# ----- Keyword Arguments -----
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Siddhi", role="Python Developer", city="Mumbai")

# ----- Mixed Arguments -----
def full_details(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

full_details(10, 20, 30, 40, 50, city="Mumbai", role="Developer", level="Beginner")

# ----- Functions with Return -----
def multiply_two(a, b):
    return a * b

x = multiply_two(5, 6)
print(x)

def details():
    return "Siddhi", 21, "Python Developer"

name, age, role = details()
print(name, age, role)

def calculate_total(price, quantity):
    total = price * quantity
    return total

bill = calculate_total(250, 3)
print("Your bill is:", bill)

# ==============================================================
# 3️. DICTIONARIES: Key-Value Pairs for Organized Data
# ==============================================================

# ----- Basic Dictionary Operations -----
student = {"name": "Siddhi", "age": 21, "city": "Mumbai"}
print(student)
print(student["name"])
print(student.get("city"))

student["course"] = "Python Developer"
student["age"] = 22
print(student)

removed_value = student.pop("city")
print("Removed:", removed_value)
print(student)

last_removed = student.popitem()
print("Last removed:", last_removed)
print(student)

if "name" in student:
    print("Name key exists!")

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ":", value)

student.update({"name": "Siddhi Katkar", "city": "Pune"})
print(student)
print(student.keys())
print(student.values())
print(student.items())

student.clear()
print(student)

new_student = student.copy()
print(new_student)

# ----- Nested Dictionaries -----
students = {
    "s1": {"name": "Siddhi", "marks": 88},
    "s2": {"name": "Riya", "marks": 92}
}

print(students["s1"]["name"])

student = {"name": "Siddhi"}
student.setdefault("age", 21)
student.setdefault("name", "New")
print(student)

# ==============================================================
# 4️. WORKING WITH STRINGS: Methods and Formatting
# ==============================================================

# ----- String Methods -----
text = "python programming"
print(text.upper())
print(text.lower())
print(text.title())

sentence = "Python is fun"
words = sentence.split()
print(words)
new_sentence = "-".join(words)
print(new_sentence)
text = "I like Java"
print(text.replace("Java", "Python"))
text = "   Hello World   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# ----- String Formatting -----
name = "Siddhi"
age = 21
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

# ----- Reverse String -----
s = "Siddhi"
rev = ""
for char in s:
    rev = char + rev
print(rev)

# ----- Count Vowels -----
s = "Siddhi Katkar"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# ----- Palindrome Check -----
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ----- Count Words -----
sentence = "I am learning Python"
words = sentence.split()
print(len(words))

# ----- Remove Spaces -----
s = "my name is siddhi"
print(s.replace(" ", ""))

# ==============================================================
# 5️. SCOPE: Local vs Global Variables
# ==============================================================

def greet():
    message = "Hello World"
    print(message)

greet()

message = "Hello World"
def greet_global():
    print(message)

greet_global()
print(message)

# ----- Global Variable Manipulation -----
count = 0
def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
print("Outside function:", count)

name = "Siddhi"
def function1():
    print("my name is:",name)
def function2():
    global name
    name = "Bharvi"
    print("Inside function:",name)

function2()
print("Outside function", name)

# ==============================================================
# 6️. BUILT-IN MODULES
# ==============================================================

# ----- Math Module -----
import math
print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2,3))
print(math.pi)

# ----- Random Module -----
import random
print(random.randint(1,10))
colors = ["red","blue","green"]
print(random.choice(colors))
nums = [1,2,3,4]
random.shuffle(nums)
print(nums)
print(random.random())

# ----- Datetime Module -----
from datetime import datetime
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))

# ----- OS Module -----
import os
print(os.listdir())
# os.remove("file.txt")  # commented for safety
print(os.path.exists("data.txt"))
# os.mkdir("new_folder") # commented for safety
print(os.getcwd())

# ==============================================================
# 🛠️ HANDS-ON PRACTICE
# ==============================================================

# --------------------------------------------------------------
# 1️. CURRENCY CONVERTER
# --------------------------------------------------------------

# ----- Conversion Rates -----
conversion_rates = {
    "USD": 1.0,       
    "INR": 82.5,      
    "EUR": 0.92,      
    "GBP": 0.81,      
    "JPY": 145.3      
}

# ----- Show Available Currencies -----
def show_currencies():
    print("\nAvailable currencies:")
    for currency in conversion_rates:
        print(currency, end="  ")
    print("\n")

# ----- Currency Conversion Function -----
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in conversion_rates:
        print(f"Sorry, {from_currency} is not supported.")
        return None
    if to_currency not in conversion_rates:
        print(f"Sorry, {to_currency} is not supported.")
        return None

    amount_in_usd = amount / conversion_rates[from_currency]
    converted_amount = amount_in_usd * conversion_rates[to_currency]

    return converted_amount

# ----- Main Converter Function -----
def currency_converter():
    while True:
        show_currencies()
        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., INR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            print(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")

        choice = input("\nDo you want to convert another amount? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the currency converter!")
            break

currency_converter()

# --------------------------------------------------------------
# 2️. STUDENT DATABASE USING DICTIONARIES
# --------------------------------------------------------------

students = {}

# ----- Add Student -----
def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!\n")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    students[roll] = {"name": name, "age": age, "city": city}
    print("Student added successfully!\n")

# ----- Update Student -----
def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print("Student not found!\n")
        return
    print("1. Name\n2. Age\n3. City\n4. Update all")
    choice = input("Enter choice: ")
    if choice == "1":
        students[roll]["name"] = input("Enter new name: ")
    elif choice == "2":
        students[roll]["age"] = input("Enter new age: ")
    elif choice == "3":
        students[roll]["city"] = input("Enter new city: ")
    elif choice == "4":
        students[roll].update({
            "name": input("Enter new name: "),
            "age": input("Enter new age: "),
            "city": input("Enter new city: ")
        })
    else:
        print("Invalid choice!")
        return
    print("Student updated successfully!\n")

# ----- Delete Student -----
def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")
    removed = students.pop(roll, None)
    if removed:
        print(f"Student removed: {removed}\n")
    else:
        print("Student not found!\n")

# ----- Search Student -----
def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")
    data = students.get(roll)
    if data:
        print("\nStudent Found:")
        for key, val in data.items():
            print(f"{key}: {val}")
        print()
    else:
        print("Student not found!\n")

# ----- View All Students -----
def view_all_students():
    print("\n--- All Students ---")
    if not students:
        print("No student records found.\n")
        return
    for roll, info in students.items():
        print(f"\nRoll No: {roll}")
        for k, v in info.items():
            print(f"{k}: {v}")
    print()

# ----- Main Menu -----
def main_menu():
    while True:
        print("\n==============================")
        print("STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View All Students")
        print("6. Exit")
        print("==============================")
        
        option = input("Enter your choice: ")
        
        if option == "1":
            add_student()
        elif option == "2":
            update_student()
        elif option == "3":
            delete_student()
        elif option == "4":
            search_student()
        elif option == "5":
            view_all_students()
        elif option == "6":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid input! Try again.")

# main_menu()

# --------------------------------------------------------------
# 3️. TEXT ANALYZER (Count Words / Characters / Frequency)
# --------------------------------------------------------------

# ----- Get Input from User -----
text = input("Enter your text:\n")

# ----- Character and Word Count -----
total_chars = len(text)
chars_no_spaces = len(text.replace(" ", ""))
words = text.split()
total_words = len(words)

# ----- Average Word Length -----
if total_words > 0:
    avg_word_length = chars_no_spaces / total_words
else:
    avg_word_length = 0

# ----- Count Sentences -----
sentences = text.count('.') + text.count('!') + text.count('?')

# ----- Count Paragraphs -----
paragraphs = text.split("\n")
total_paragraphs = len(paragraphs)

# ----- Word Frequency -----
word_freq = {}
for word in words:
    word = word.lower().strip(".,!?")
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# ----- Print Results -----
print("\n--- TEXT ANALYSIS RESULTS ---")
print("Total characters (including spaces):", total_chars)
print("Total characters (excluding spaces):", chars_no_spaces)
print("Total words:", total_words)
print("Average word length:", round(avg_word_length, 2))
print("Total sentences:", sentences)
print("Total paragraphs:", total_paragraphs)

print("\nWord Frequency:")
for word, freq in word_freq.items():
    print(f"{word} : {freq}")

# --------------------------------------------------------------
# 4️. BANK ACCOUNT SYSTEM
# --------------------------------------------------------------

# ----- Account Dictionary -----
account = {
    "name": "Siddhi",
    "balance": 0
}

# ----- Show Account Details -----
def show_details():
    print("\n--- ACCOUNT DETAILS ---")
    print("Account Holder:", account["name"])
    print("Balance:", account["balance"])

# ----- Deposit Money -----
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        account["balance"] += amount
        print(f"Deposited {amount}. New balance is {account['balance']}.")
    else:
        print("Invalid amount! Must be greater than 0.")

# ----- Withdraw Money -----
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount > account["balance"]:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid amount!")
    else:
        account["balance"] -= amount
        print(f"Withdrawn {amount}. Remaining balance is {account['balance']}.")

# ----- Main Bank Menu -----
while True:
    print("\n--- BANK MENU ---")
    print("1. Show Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_details()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
