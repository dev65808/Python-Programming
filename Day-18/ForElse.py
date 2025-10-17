successful = True
for number in range(3):
    print("Attempt")  # executed
    if successful:
        print("successful")  # executed
        break


successful = False
for number in range(3):
    print("Attempt")  # executed 3 times
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")  # executed
