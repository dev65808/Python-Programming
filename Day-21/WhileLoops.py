number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)  # only quit form will work

command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)  # only quit and QUIT form will work

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)  # if we write quit in any form it will work
