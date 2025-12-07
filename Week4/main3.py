# SECTION 4 — Organizing Code Into Multiple Files
# helpers2.py #file_ops.py #logic.py are related files of this file 

from logic import add_student, get_all_students

add_student("Siddhi", 22)
add_student("Riya", 20)

students = get_all_students()

print("Saved Students:")
for s in students:
    print(s.strip())
