# main2.py imports this file

def add(a, b):
    return a + b

def welcome(name):
    return f"Welcome {name}, you are doing great!"

def save_message(msg):
    with open("message.txt", "w") as f:
        f.write(msg)
