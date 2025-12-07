import csv
from datetime import datetime

# CSV file name
FILENAME = "expenses.csv"

# ---------------------------------------------------------
# Load expenses from CSV file
# ---------------------------------------------------------
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert date from YYYY-MM-DD to DD-MM-YYYY for display
                try:
                    date_obj = datetime.strptime(row['Date'], "%Y-%m-%d")
                    row['Date'] = date_obj.strftime("%d-%m-%Y")
                except:
                    pass  # Keep original if format is unexpected
                expenses.append(row)
    except FileNotFoundError:
        # Create CSV with headers if it doesn't exist
        with open(FILENAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Date","Category","Description","Amount","Payment_Method","Notes"])
            writer.writeheader()
    return expenses

# ---------------------------------------------------------
# Add a single expense
# ---------------------------------------------------------
def add_expense(expenses, date, category, amount, note, description=None, payment_method=None):
    expense = {
        "Date": date,
        "Category": category,
        "Description": description if description else "",
        "Amount": amount,
        "Payment_Method": payment_method if payment_method else "",
        "Notes": note if note else ""
    }
    expenses.append(expense)

# ---------------------------------------------------------
# Save list back to CSV file
# ---------------------------------------------------------
def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        fieldnames = ["Date","Category","Description","Amount","Payment_Method","Notes"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            # Convert date back to YYYY-MM-DD for CSV consistency
            try:
                date_obj = datetime.strptime(exp['Date'], "%d-%m-%Y")
                exp_date = date_obj.strftime("%Y-%m-%d")
            except:
                exp_date = exp['Date']
            writer.writerow({
                "Date": exp_date,
                "Category": exp['Category'],
                "Description": exp.get('Description', ""),
                "Amount": exp['Amount'],
                "Payment_Method": exp.get('Payment_Method', ""),
                "Notes": exp.get('Notes', "")
            })

# ---------------------------------------------------------
# MAIN PROGRAM WITH MENU
# ---------------------------------------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Input all 6 fields
            date_input = input("Enter date (DD-MM-YYYY): ")
            try:
                date_obj = datetime.strptime(date_input, "%d-%m-%Y")
                date = date_obj.strftime("%d-%m-%Y")
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY.")
                continue

            category = input("Enter category (Food, Travel, Shopping, etc.): ")
            amount = input("Enter amount: ")
            description = input("Enter description (optional, press Enter to skip): ")
            payment_method = input("Enter payment method (optional, e.g., Cash, Card, UPI): ")
            note = input("Enter note (optional, press Enter to skip): ")

            add_expense(expenses, date, category, amount, note, description, payment_method)
            save_expenses(expenses)
            print("\n Expense added successfully!")

        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses recorded.")
            else:
                print("\n--- All Expenses ---")
                print("Date       | Category   | Amount | Description           | Payment Method | Notes")
                print("---------------------------------------------------------------------------------")
                for exp in expenses:
                    print(f"{exp['Date']} | {exp['Category']} | {exp['Amount']} | "
                          f"{exp.get('Description','')} | {exp.get('Payment_Method','')} | {exp.get('Notes','')}")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
