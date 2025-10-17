# Scenario-1
temperature = 35
if temperature > 30:
    print("It's warm")  # executed
    print("Drink water")  # excecuted
print("Done")  # executed

# Scenario-2
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")  # only this will be executed

# Scenario-3
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")  # executed
print("Done")  # executed
