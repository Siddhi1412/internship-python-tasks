# SECTION 4 — Organizing Code Into Multiple Files
# utils.py used

from utils import add, welcome, save_message

# 1. use add() → returns a value → print it
result = add(10, 20)
print("Addition result:", result)

# 2. use welcome() → returns text → print it
print(welcome("Siddhi"))

# 3. use save_message() → ACTION function → no print
save_message("This message is saved into file!")
