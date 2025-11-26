##Create a number guessing game
import random

# Computer chooses a random number between 1 and 50
secret_number = random.randint(1, 50)

guess = 0  # initialize user's guess
attempts = 0  # initialize counter

while guess != secret_number:
    try:
        guess = int(input("Guess the number between 1 and 50: "))
        attempts += 1  # increment counter on each guess

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")

print(f"Congratulations! You guessed it in {attempts} attempts. The number was {secret_number}.")


#Build a program that categorizes ages (child, teen, adult)

# type 1 - simple
age = int(input("Enter your age: "))

# Check category
if age >= 0 and age <= 12:
    print("You are a Child.")
elif age >= 13 and age <= 19:
    print("You are a Teen.")
elif age >= 20:
    print("You are an Adult.")
else:
    print("Invalid age entered.")

#type 2
while True:
    age= input("Enter your age (or type 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    
    if age <=0:
        print("you're not yet born")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age >= 20:
        print("You are an Adult.")
    else:
        print("Invalid age entered.")


# type3
age_categories = []

age = int(input("enter your age:"))

if age <= 0:
    print("Enter a valid age please")

else:
    if age <=12:
        category = "child"

    elif age <=19:
        category = "teen"

    elif age <=50:
        category = "adult"
        
    else:
        category = "senior_citizen"
    
    age_categories.append({"age": age , "category" : category})
    print("Results so far:" , age_categories)



# type4

age_categories = []

while True :
    age_input =input("Enter your age: ")

    if age_input.lower() == 'quit':
        break

    if not age_input.isdigit():
        print("please enter a valid number")
        continue #if input is not valid ,we skip the rest of the loop and ask for input again

    age = int(age_input)

    if age<=0:
        print("please enter a valid age")
        continue

    if age<=12:
        category = "child"

    elif age <=19:
        category = "teenage"

    elif age<= 50:
        category = "adult"

    else :
        category = "senior_citizen"

    age_categories.append({"age": age , "category":category})
    print("results so far:" , age_categories)

print("\nFinal Results:" ,age_categories)



#Make a shopping list manager with add/remove items
# TYPE 1
shopping_list = []

while True:
    print("Shopping list manager")
    print("1.Add an item")
    print("2.Remove an Item")
    print("3.View list")
    print("4.Quit")

    choice = input("enter your choice(1-4): ")

    if choice == '1':
        item = input("Enter the item to add:")
        shopping_list.append(item)
        print(f" '{item}' added to the list")

    elif choice == '2':
        item = input("enter the item to remove : ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed form the list")

        else:
            print(f"'{item}'not found in the list")

    elif choice == '3':
        if shopping_list:
            print("current shopping list",shopping_list)

        else:
            print("your shopping list is empty")

    elif choice == '4':
        print("exiting the Shopping List ,GOODBYE!")
        break

    else:
        print("Invalid choice.Please enter 1-4")


# TYPE 2
# shopping_list = []

# while True:
#     print("\n===== Shopping List Manager =====")
#     print("1. Add an item")
#     print("2. Remove an item (by number)")
#     print("3. View list")
#     print("4. Quit")
#     print("================================")

#     choice = input("Enter your choice (1-4): ")

#     # 1️. ADD ITEM
#     if choice == '1':
#         item = input("Enter the item to add: ").strip()

#         if item == "":
#             print("Item cannot be empty!")
#             continue
        
#         if item.lower() in [i.lower() for i in shopping_list]:
#             print(f"'{item}' is already in the list (duplicates not allowed).")
#         else:
#             shopping_list.append(item)
#             print(f"'{item}' added successfully!")

#     # 2️. REMOVE ITEM BY NUMBER
#     elif choice == '2':
#         if not shopping_list:
#             print("Your shopping list is empty. Nothing to remove.")
#             continue
        
#         print("\nYour Shopping List:")
#         for i, item in enumerate(shopping_list, start=1):
#             print(f"{i}. {item}")

#         index_input = input("Enter the item number to remove: ")

#         if not index_input.isdigit():
#             print("Please enter a valid number.")
#             continue

#         index = int(index_input)

#         if 1 <= index <= len(shopping_list):
#             removed_item = shopping_list.pop(index-1)
#             print(f"'{removed_item}' removed successfully!")
#         else:
#             print("Invalid item number.")

#     # 3️. VIEW LIST
#     elif choice == '3':
#         if shopping_list:
#             print("\nYour Shopping List:")
#             for i, item in enumerate(shopping_list, start=1):
#                 print(f"{i}. {item}")
#         else:
#             print("Your shopping list is empty.")

#     # 4️. QUIT
#     elif choice == '4':
#         print("Thank you for using the Shopping List Manager!")
#         break

#     else:
#         print("Invalid choice! Please enter a number from 1 to 4.")


##Create a multiplication table generator
# type1
num = int(input("Enter a number: "))

for i in range(1, 11):        # Loop from 1 to 10
    print(f"{num} x {i} = {num * i}")



# type 2
while True:
    print("\nMultiplication Table Generator")

    # Take number
    num_input = input("Enter the number you want the table for (or 'quit' to exit): ")

    if num_input.lower() == 'quit':
        print("Thank you for using the Table Generator!")
        break
    
    if not num_input.isdigit():
        print("Please enter a valid number!")
        continue

    num = int(num_input)

    # Take starting range
    start = int(input("Enter start of range: "))

    # Take ending range
    end = int(input("Enter end of range: "))

    print(f"\n Multiplication Table of {num} from {start} to {end}")
    print("THANK YOU")

    for i in range(start, end + 1):
        print(f"{num} x {i} = {num * i}")


##Build a simple login system with username/password##
#type 1

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")

#type 2 
correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Wrong credentials! Attempts left: {attempts}")

if attempts == 0:
    print("Account locked! Too many failed attempts.")


#type-3#
users = {
    "siddhi": "python123",
    "admin": "1234",
    "test": "abcd"
}

username = input("Enter username: ")

if username in users:   #checking if username exists

    password = input("Enter password: ")
    
    if password == users[username]:
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("Username does not exist!")



# Practice with different list operations and methods
fruits = ["apple", "cherry", "banana", "mango","cherry"]

# # Add item
fruits.append("chickoo")


# # Insert item at position
fruits.insert(1,"grapes")



# # Remove item by name
fruits.remove("banana")


# # Sorting
fruits.sort()


# # Remove item by index
removed = fruits.pop(2)
print("Removed :",removed)
print(fruits)

# # Sorting
fruits.sort()


# # Reverse list
fruits.reverse()


# # Sorting
fruits.sort()


# #clear everything in the list
fruits.clear()


# # knowing the position of an item
print(fruits.index("mango"))

# #Count how many times item appears
print(fruits.count("cherry"))

# total items
print(len(fruits))

print(fruits)


# List Practice Menu Program
items = []

while True:
    print("\n===== List Operations Menu =====")
    print("1. Add item")
    print("2. Insert item at position")
    print("3. Remove item")
    print("4. Pop item by index")
    print("5. View list")
    print("6. Sort list")
    print("7. Reverse list")
    print("8. Clear list")
    print("9. Quit")

    choice = input("Enter choice (1-9): ")

    if choice == "1":
        item = input("Enter item to add: ")
        items.append(item)
        print("Added!")

    elif choice == "2":
        item = input("Enter item to insert: ")
        index = int(input("Enter position: "))
        items.insert(index, item)
        print("Inserted!")

    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item)
            print("Removed!")
        else:
            print("Item not found!")
    
    elif choice == "4":
        index = int(input("Enter index to pop: "))
        if 0 <= index < len(items):
            removed = items.pop(index)
            print(f"Popped: {removed}")
        else:
            print("Invalid index!")

    elif choice == "5":
        print("Current List:", items)

    elif choice == "6":
        items.sort()
        print("Sorted!")

    elif choice == "7":
        items.reverse()
        print("Reversed!")

    elif choice == "8":
        items.clear()
        print("List cleared!")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")





############################
items = []

while True:
    print("\nList Operations Menu")
    print("1. Add item")
    print("2. Insert item at position")
    print("3. Remove item")
    print("4. Pop item by index")
    print("5. View list")
    print("6. Sort list")
    print("7. Reverse list")
    print("8. Clear list")
    print("9. Quit")

    choice = input("Enter choice (1-9): ")

    if choice == "1":
        item = input("Enter item to add: ")
        items.append(item)
        print("Added!")

    elif choice == "2":
        item = input("Enter item to insert: ")
        index = int(input("Enter position: "))
        items.insert(index, item)
        print("Inserted!")

    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item)
            print("Removed!")
        else:
            print("Item not found!")
    
    elif choice == "4":
        index = int(input("Enter index to pop: "))
        if 0 <= index < len(items):
            removed = items.pop(index)
            print(f"Popped: {removed}")
        else:
            print("Invalid index!")

    elif choice == "5":
        print("Current List:", items)

    elif choice == "6":
        items.sort()
        print("Sorted!")

    elif choice == "7":
        items.reverse()
        print("Reversed!")

    elif choice == "8":
        items.clear()
        print("List cleared!")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")


