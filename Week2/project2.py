# Build a Student Grade Calculator that takes marks and returns grade with comments, and stores results in a list


results = []   # Store all student data

while True:
    print("\n Student Grade Calculator")
    name = input("Enter student name (or type 'quit' to stop): ").strip()

    if name.lower() == "quit":
        break

    # Take marks
    marks_input = input("Enter marks (0-100): ")

    if not marks_input.isdigit():
        print("Please enter a valid number for marks!")
        continue

    marks = int(marks_input)

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100!")
        continue

    # Grade Logic
    if marks >= 90:
        grade = "A"
        comment = "Excellent performance!"
    elif marks >= 75:
        grade = "B"
        comment = "Good job, keep it up!"
    elif marks >= 60:
        grade = "C"
        comment = "Fair performance, can improve."
    elif marks >= 40:
        grade = "D"
        comment = "Need to work harder!"
    else:
        grade = "F"
        comment = "Failed. Better luck next time."

    # Store result
    student = {
        "name": name,
        "marks": marks,
        "grade": grade,
        "comment": comment
    }

    results.append(student)

    print(f"\n{name}'s Result:")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Comment: {comment}")

# After quitting:
print("\n FINAL RESULTS")
for r in results:
    print(f"{r['name']} - Marks: {r['marks']} | Grade: {r['grade']} | Comment: {r['comment']}")
