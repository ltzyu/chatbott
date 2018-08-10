import random

poss = ["iteration", "programming", "algorithm", "lists"]
answer = random.choice(list(poss)).upper()

guesses = []
maxfails = 7
display = []

def check(answer, guesses, guess):
    guess = guess.upper()
    status = ' '
    for letter in answer:
        if letter in guesses:
            status += letter
        else:
            status += "_ "

def intro():
    display.extend(answer)
    for x in range(len(display)):
        display[x] = "_ "
        print(('').join(display))
        print("\n\n")

def main():
    intro()
    check(answer, guesses, guess)

if __name__ == "__main__":
    main()
