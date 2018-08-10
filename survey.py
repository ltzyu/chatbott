def responses():
    responses = {

    }
    name = input("Name")
    age = int(input("Age"))
    siblings = input("Do you have siblings?")
    fish = input("Favorite fish")
    almonds = input("Almonds?")
    frogs = input("Frogs?")
    afrogs = input("Almond frogs?????")

    responses[name] = age, age, siblings, fish, almonds, frogs, afrogs
    print(responses)

i = 0
while True:
    responses()
    i += 1
    print("Responses Recorded:")
    print(i)
