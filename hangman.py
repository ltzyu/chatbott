import random

poss = ["notebook", "phone", "computer", "chair", "office", "cubicle", "beanbag", "mouse", "suitcase", "hairbrush"]
answer = random.choice(list(poss))


def check(answer, guesses, guess):
    guess = guess
    status = ' '
    i = 0
    matches = 0

    for letter in answer:
        if letter in guesses:
            status += letter
        else:
            status += ""
        if letter == guess:
            matches += 1
    else:
        print("Next letter")

#    if matches > 1:
#print("Nice")
#    elif matches == 1:
#        print("Nice")
#    else:
#        print("Word:")
    return status

def main():
    guesses = []
    guessed = False
    print('The word contains', len(answer), 'letters')
    i = 0
    while i <10:
        while not guessed:
            print("Enter letter or word")
            guess = input()
            if guess in guesses:
                print("Already guessed")
            elif len(guess) == len(answer):
                if guess == answer:
                    guessed = True
                    print("That's the word! Congrats")

            elif len(guess) == 1:
                guesses.append(guess)
                result = check(answer, guesses, guessed)
                if result == answer:
                    guessed = True
                    print("That's right!")
                    break
                else:
                    print(result)
            else:
                print("Invalid entry")

main()

if __name__ == "__main__":
    main()
