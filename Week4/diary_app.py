# HANDS-ON
# 2] Build a simple diary application

# --------------------------
# TYPE 1 - BASIC
# --------------------------
entry = input("Write your diary entry: ")

try:
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("Diary entry saved!")
except Exception as e:
    print("Error:", e)


# --------------------------
# TYPE 2 - ADVANCED - Diary App With Date and Time
# --------------------------
from datetime import datetime

entry = input("Write your diary entry: ")
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    with open("diary.txt", "a") as file:
        file.write(f"{date} - {entry}\n")
    print("Diary entry saved with date and time!")
except Exception as e:
    print("Error:", e)
