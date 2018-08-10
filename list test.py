import random

#print("Your numbers")
#aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(aList)
#print(aList[3])
#print(8 in aList)
#print(len(aList))

#print("Your letter:")
bList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bList[:: -1]) #prints the list in reverse in increments of 1 (-1 bc backwards)

#print("Who do I lov?")
cList = ["u", "Robin", "Klein", "Tiki", "Robin", "Robin", "u"]
#print(random.choice(cList))

print("VOTING GAUNTLET")
print("Who will win?")
dList = ["Marth", "Hardin", "Sigurd", "Arvis", "Ephraim", "Lyon", "Ike", "Zelgius"]
print(dList)
#answer = random.choice(dList)
answer = input()
i = 0
while i < 3:
    print("...")
    i += 1
    continue
print(answer)
print("...")
print("You really think so?")
print("Well, Good Luck!")

i = 0
while i < 4:
    print("")
    i += 1
    continue

print("Who is your favorite?")
eList = ["Robin", "Robin", "Robin", "Robin"]
print(eList)
answer1 = input()
i = 0
while i < 2:
    print("...")
    i += 1
    continue
print(answer1)
print("...")
print("Of course! Who else would it be")
print("!")
print("You have good taste ^^")

i = 0
while i < 4:
    print("")
    i += 1
    continue

i = 0
while i < 2:
    print("Should you fodder Klein?")
    answer2 = input()
    if answer2 == "yes":
        print("Wrong answer, TRY AGAIN")
        i += 1
        continue
    else:
        if answer2 == "no":
            print("That's right! He's a great unit...we all love Klein here.")
            break
i = 0
while i < 4:
    print("")
    i += 1
    continue
