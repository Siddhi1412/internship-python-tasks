## Conditional statements: if, elif, else

age= int(input("Enter your age : "))

if age<0:
    print("enter a valif age")

elif age <12 :
    print("You're a child")

elif age < 17:
    print("You're a teenager")

elif age < 59:
    print("You're an adult")

else:
    print("You're a senior")


## Comparison operators: ==, !=, >, <, >=, <=
a = 10
b = 5

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

## Lists: creating, accessing, modifying collections of data

fruits = ["apple", "banana", "mango"]
print("Full list:", fruits)

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# append - inserts at specific position
fruits.append("orange")
print("After adding:", fruits)

# removes -removing by actual name  vs pop - removes by index 
fruits.remove("banana")
print("After removing banana:", fruits)

# insert at a specific position
fruits.insert(1, "kiwi")
print(fruits)

# remove by index  wheres as "Remove" removes by name
fruits.pop(2)  
print(fruits)


print("Length of list:", len(fruits))

print("Looping through list:")
for fruit in fruits:
    print(" -", fruit)


## For loops: repeating actions with lists
numbers = [10, 20, 30]

for n in numbers:
    print("Value:", n)

# range
for i in range(5):
    print("Loop number:", i)

for i in range(1,6):
    print(i)


# Loop with Index
colors = ["red", "blue", "green"]

for index in range(len(colors)):
    print(index, "-", colors[index])

    # using enumerate()
for index, color in enumerate(colors):
    print(index, "-", color)



## while loop
    count = 1
    while count<=5:
        print("count is: ",count)
        count +=1

# user input until correct
password = "abc123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")
    if user_input != password:
        print("Incorrect, try again!")

print("Access granted!")

# Print numbers from 10 to 1 using while loop
a = 10

while a >= 1:
    print("number are:" ,a)
    a -= 1


# counting down
start = int(input("Enter a starting number: "))

# Countdown using while loop
while start >= 1:
    print("Counting down:", start)
    start -= 1  # subtract 1 each time

print("Countdown finished!")


# counting up
end = int(input("Enter a number to count up to: "))

i = 1  # start counting from 1

while i <= end:
    print("Counting up:", i)
    i += 1  # increase by 1 each time

print("Counting finished!")




# combined start and end i.e count up(+) and count down (-)

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


# Count Up or Down with Custom Step


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step (positive number): "))   #instead of incrementing by 1 ,we can increment by much we want to jump forward

# Ensure step is positive
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


# #try-except

# try-except  1
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Oops! That is not a valid number.")

# try-except 2
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# try-except 3 
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be positive!")
        else:
            print("Your age is:", age)
            break  # exit the loop when input is valid
    except ValueError:
        print("Invalid input! Please enter a number.")
