# HANDS-ON
# 4] Create a quiz game that saves scores

print("Welcome to the Quiz Game!")

# --------------------------
# Questions List
# --------------------------
questions = [
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is the capital of India?", "answer": "delhi"},
    {"question": "Who developed Python?", "answer": "guido van rossum"},
    {"question": "What is 10 / 2?", "answer": "5"},
    {"question": "What is the color of the sky?", "answer": "blue"}
]

score = 0

# --------------------------
# Ask each question
# --------------------------
for q in questions:
    user_answer = input(q["question"] + " ").lower()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"Correct answer is: {q['answer']}\n")

print(f"\nYour final score is: {score}/{len(questions)}")

# --------------------------
# Save score to file
# --------------------------
try:
    with open("quiz_scores.txt", "a") as file:
        file.write(f"Score: {score}/{len(questions)}\n")
    print("Your score has been saved to quiz_scores.txt")
except Exception as e:
    print("Error saving score:", e)

# --------------------------
# View past scores
# --------------------------
view = input("Do you want to see your past scores? (yes/no): ").lower()

if view == "yes":
    try:
        print("\nPrevious Scores:")
        with open("quiz_scores.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No past scores found.")
