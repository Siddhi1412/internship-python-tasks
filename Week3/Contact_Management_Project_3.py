# CONTACT MANAGEMENT SYSTEM

# 1. Dictionary to store contacts
contacts = {}

# 2. Function to add a new contact
def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    key = name.lower()  # Convert to lowercase for storage

    if key in contacts:
        print("Contact already exists!")
    else:
        contacts[key] = phone
        print("Contact added successfully!")

# 3. Function to search for a contact
def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ").lower()  # Convert input to lowercase

    if name in contacts:
        print(f"{name.title()} : {contacts[name]}")
    else:
        print("Contact not found!")

# 4. Function to display all contacts
def display_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"{name.title()} : {phone}")   # Display clean formatted name

# 5. Main menu
def main_menu():
    while True:
        print("\n===== CONTACT MANAGEMENT MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting Contact Manager...")
            break
        else:
            print("Invalid choice! Try again.")

# Run the menu
main_menu()
