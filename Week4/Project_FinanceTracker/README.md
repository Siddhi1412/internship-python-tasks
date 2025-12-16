# 💰 Personal Finance Tracker

A **command-line Personal Finance Tracker** built using Python that allows users to record, store, view, and analyze daily expenses using a CSV file.  
The project demonstrates file handling, modular programming, and basic reporting logic.

---

## 📌 Features

- Add daily expenses with details such as:
  - Date
  - Category
  - Amount
  - Description
  - Payment Method
  - Notes
- View all stored expenses from a CSV file
- Automatically creates the CSV file if it does not exist
- Monthly expense report generation
- Modular code structure for better readability and maintenance

---

## 🛠️ Technologies Used

- Python
- CSV module
- datetime module

---

## 📂 Project Structure

```text
personal-finance-tracker/
│
├── main.py        # Main application with menu-driven interface
├── data_ops.py   # Handles CSV data loading, saving, and insertion
├── reports.py    # Generates monthly expense reports
├── expenses.csv  # Stores all expense records
└── README.md     # Project documentation
```

---

## ▶️ How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/personal-finance-tracker.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd personal-finance-tracker
   ```

3. **Run the main program**
   ```bash
   python main.py
   ```

---

## 🧾 Application Menu

```
===== PERSONAL FINANCE TRACKER =====
1. Add Expense
2. View All Expenses
3. Exit
```

---

## 🗂️ File Overview

### `main.py`
- Acts as the entry point of the application
- Displays menu options
- Accepts user input
- Calls functions to add and display expenses
- Handles date formatting and validation

### `data_ops.py`
- Manages CSV file operations
- Loads expenses from `expenses.csv`
- Adds new expense records
- Saves updated data back to the CSV file

### `reports.py`
- Generates monthly expense reports
- Calculates total expenses for a given month and year
- Displays categorized expense details

### `expenses.csv`
- Stores expense data persistently
- Columns include:
  - Date
  - Category
  - Description
  - Amount
  - Payment_Method
  - Notes

---

## 📊 Sample CSV Format

```csv
Date,Category,Description,Amount,Payment_Method,Notes
2025-12-01,Food,Birthday Celebration,1200,UPI,Friends Gathering
```

---

## 🚀 Future Enhancements

- Category-wise expense analysis
- Expense filtering and sorting
- Data visualization using charts
- GUI or web-based version using Flask
- Export monthly reports

---

## 👩‍💻 Author

**Siddhi Katkar**  
Python Learner | Aspiring Software & Data Professional  

---

## 📌 Note

This project is suitable for:
- Python beginners
- Internship / academic submissions
- Demonstrating file handling and modular programming concepts
