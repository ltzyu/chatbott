print("NOTICE: All answers are LOWER CASE in this game.")
print("...")
print("Welcome to TERA?")
print("...")
print("...")
print("...")
print("Gobo and Tera are wandering through the woods, lost.")
print("Night has fallen and rain is starting to fall.")
print("There is a DARK CASTLE looming in the distance")
print("Tera: Ah! Look over there!")
print("Gobo and Tera approach the DARK CASTLE")
print("Tera: Finally! Shelter")
print("Gobo: Tera are you sure? Looks shady to me")
print("Tera: I'm sure it'll be fine")
print("The two enter the castle despite Gobo's complaints")
print("Tera: Wait here Gobo, I'm going to go look for the owner. I'll be right back")
print("...")
print("...")
print("......")
print("Gobo: Tera's been gone for a while now, I'd better go look for her")

item = 0
i = 0
while i < 2:
    print("There are two halls, should I go left or right?")
    print("LEFT or RIGHT")
    answer = input()
    if answer == "left":
        print("Gobo: It's a dead end, let's go back.")
        i += 1
        continue
    else:
        if answer == "right":
            print("Gobo: It's a long hall huh")
            print("Gobo: Oh no! Another pathway!")
            break
i = 0
while i < 3:
    print("Gobo: Should I take the left, center, or right hallway")
    print("LEFT, CENTER, or RIGHT")
    answer1 = input()
    if answer1 == "left":
        print("Gobo: It's another dead end...let's try the other paths.")
        i += 1
        continue
    elif answer1 == "center":
            print("Gobo: Another fork!")
            print("Gobo: Should I go into the dark hall or the light hall?")
            print("DARK or LIGHT")
            answer3 = input()
            if answer3 == "dark":
                print("Gobo: AH")
                print("Gobo: A MONSTER!")
                if item == 0:
                    print("The MONSTER attacks, and Gobo, weaponless, is helpless to defend himself.")
                    print("Maybe if Gobo had a WEAPON of some sort, things would have ended differently.")
                    print("You died. THE END")
                break
                if item == 1:
                    print("Gobo defeats the MONSTER")
                    print("Whew that was tough! Tera could be in danger though, let's hurry!")
                continue
            elif answer3 == "light":
                print("There is a SWORD in the stone")
                print("Gobo has obtained SWORD")
                print("This could be useful...let's go back, Tera's waiting for me somewhere...")
                item = item + 1
            i+= 1
            continue
    else:
        if answer1 == "right":
            print("Tera is trapped in a cell with a GHOUL")
            print("Gobo: TERA!")
            print("Tera: Gobo! It isn't safe here!")
            print("Tera: Run while you can! Just leave me...leave me so you can live...")
            print("Gobo: Tera...")
            print("Save Tera?")
            print("YES or NO")
            answer2 = input()
            if answer2 == "yes":
                if item == 1:
                    print("The SWORD pierces through the monster, saving Tera")
                    print("Gobo and Tera hurriedly escape the castle to safety")
                    print("Congratulations! You've led both of them to safety!")
                    break
                if item == 0:
                    print("Weaponless, Gobo is helpless to save Tera despite his efforts")
                    print("Maybe if Gobo had a WEAPON of some sort, things would have ended differently.")
                    print("You died. THE END")
                break
            elif answer2 == "no":
                print("Gobo escapes to his own safety outside, leaving Tera behind.")
                print("Distantly, screams could be heard")
                if item == 1:
                    print("Gobo: Maybe with this SWORD I could have saved Tera...")
                    print("Gobo: and she wouldn't have...")
                    print("Gobo: ...")
                    print("Gobo: ...")
                    print("......")
                    print("Congratulations, you WIN! (But at what cost?)")
                    break
                if item == 0:
                    print("Gobo: ...")
                    print("Gobo: Tera...")
                    print("Gobo: ...")
                    print("......")
                    print("Congratulations, you WIN! (But at what cost?)")
                break
