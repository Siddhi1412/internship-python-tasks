# ---------------------------------------
# PROJECT 1 - Personal Information Manager
# Stores and displays user's name, age, city, and hobbies
# ---------------------------------------

# -----------------------------
# Version 1: Basic Input and Display
# -----------------------------
# Getting user details
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies: ")

# Displaying the information
print("\n--- Personal Information ---")
print("Name   :", name)
print("Age    :", age)
print("City   :", city)
print("Hobbies:", hobbies)


# -----------------------------
# Version 2: Formatted Output with Multiple Hobbies
# -----------------------------
# Asking for personal details
name = input("\nEnter your full name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Asking for multiple hobbies in one line (comma-separated)
hobbies = input("Enter your hobbies (separated by commas): ")

# Formatting the output
print("\n--- PERSONAL INFORMATION ---")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print("Hobbies:")

# Splitting hobbies by commas and displaying each hobby
hobby_list = hobbies.split(",")
for hobby in hobby_list:
    print(" -", hobby.strip())
