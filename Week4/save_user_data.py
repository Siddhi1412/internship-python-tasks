# HANDS-ON
# 1] Create a program that saves user data to a file

# -------------------------------------------------
# Loop to take multiple user inputs
# -------------------------------------------------
while True:
    # Taking input from user
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Saving data to file
    try:
        with open("user_data.txt", "a") as file:  # append mode
            file.write(f"Name: {name}, Age: {age}, Email: {email}\n")
        print("User data saved successfully!")
    except Exception as e:
        print("Error while saving data:", e)

    # Ask if user wants to add another user
    another = input("Do you want to add another user? (yes/no): ").lower()
    if another != "yes":
        break

print("All user data saved!")
