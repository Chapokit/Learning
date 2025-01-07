message = input("What is your message? ")
space = 0
for letter in message:
    print(f"{' ' * space}{letter}")
    space += 1