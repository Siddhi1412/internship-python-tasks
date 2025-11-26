# PROJECT 1 - Build a Personal Information Manager that stores and displays your name, age, city, and hobbies with formatted output


# Getting user details
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies: ")

# Displaying the information 
print("\nPersonal Information")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Hobbies:", hobbies)




# Personal Information Manager version ii

# Asking for personal details
name = input("Enter your full name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Asking for multiple hobbies in one line
hobbies = input("Enter your hobbies (separated by commas): ")

# Formatting the output
print("\n PERSONAL INFORMATION")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"City       : {city}")

print("Hobbies    :")

# Splitting hobbies by commas)
hobby_list = hobbies.split(",")

# Display each hobby
for i in hobby_list:
    print(" -", i.strip())

