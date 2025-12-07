import csv

FILENAME = "expenses.csv"

# Load expenses from CSV
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        # Create CSV with header if not exists
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Note"])
    return expenses

# Add a single expense
def add_expense(expenses, date, category, amount, note):
    expenses.append([date, category, amount, note])

# Save expenses
def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date","Category","Amount","Note"])
        writer.writerows(expenses)
