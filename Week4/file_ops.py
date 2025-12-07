# helpers2.py, main3.py, logic.py are related files of this file

def save_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")

def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()
