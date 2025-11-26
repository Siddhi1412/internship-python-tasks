# ---------------------------------------
# Python Basics Practice
# Hello World, Variables, Calculator, User Input
# ---------------------------------------

# -----------------------------
# 1. Hello World
# -----------------------------
print("Hello World!")

# -----------------------------
# 2. Variables
# -----------------------------
name = "Siddhi"      # string
age = 22             # integer
height = 5.4         # float
is_student = True    # boolean

print(name)
print(age)
print(height)
print(is_student)

# -----------------------------
# 3. Simple Calculator — Type 1
# -----------------------------
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# -----------------------------
# 4. Calculator with Validation and Loop — Type 2
# -----------------------------
def get_number(prompt):
    """Ask repeatedly until user gives a valid number."""
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("That is not a valid number. Try again.")

def choose_operation():
    """Let user pick an operation and return a symbol string."""
    ops = {"+": "Addition", "-": "Subtraction", "*": "Multiplication", "/": "Division"}
    print("\nChoose operation:")
    for sym, name in ops.items():
        print(f"  {sym} : {name}")
    while True:
        op = input("Enter +, -, * or / : ").strip()
        if op in ops:
            return op
        print("Invalid operation. Choose one of +, -, *, /.")

def calculate(a, b, op):
    """Performs calculation and handles division-by-zero."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return None
        return a / b

def main():
    print("Simple Calculator — type 'q' at any prompt to quit.")
    while True:
        first = input("Enter first number (or 'q' to quit): ").strip()
        if first.lower() == "q":
            break
        try:
            num1 = float(first)
        except ValueError:
            print("Not a number. Please try again.")
            continue

        second = input("Enter second number (or 'q' to quit): ").strip()
        if second.lower() == "q":
            break
        try:
            num2 = float(second)
        except ValueError:
            print("Not a number. Please try again.")
            continue

        op = choose_operation()
        result = calculate(num1, num2, op)
        if result is None:
            print("Error: Division by zero is not allowed.")
        else:
            # Format result to remove trailing zeros
            formatted = f"{result:.6f}".rstrip("0").rstrip(".")
            print(f"Result of {num1} {op} {num2} = {formatted}")

        cont = input("Do another calculation? (y/n): ").strip().lower()
        if cont != "y":
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()

# -----------------------------
# 5. Greeting Program
# -----------------------------
name = input("Enter your name: ")
print("Hello", name + "!")

# Or using f-string
name = input("Enter your name: ")
print(f"Hello {name} !")

# -----------------------------
# 6. Practice fixing common syntax errors
# -----------------------------
# Incorrect: print("Hello World)
# Correct:
print("Hello World")
