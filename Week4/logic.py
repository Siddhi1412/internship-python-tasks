# helpers2.py, main3.py, file_ops.py are related files of this file
from helpers2 import format_student
from file_ops import save_to_file, read_file

def add_student(name, age):
    formatted = format_student(name, age)
    save_to_file("students.txt", formatted)

def get_all_students():
    lines = read_file("students.txt")
    return lines
