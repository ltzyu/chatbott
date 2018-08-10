#from random import *
import random

def intro():
    print("Welcome to Rock-Paper-Scissors")
    print("")
    print("")
    print("NOTICE: This game is case sensitive")
    print("")
    print("Type in Rock, Paper, or Scissors and hit ENTER to begin.")

def error():
    print("Please only type in Rock, Paper, or Scissors and hit ENTER to begin.")
    print("This game is Case Sensitive.")

def response():
    aList = ["Rock", "Paper", "Scissors"]
    return random.choice(aList)

def process_input(answer):
    if answer == "Rock":
        ran = response()
        print(ran)
        if ran == "Scissors":
            print("You WIN")
        else:
            print("TRY AGAIN")
    elif answer == "Paper":
        ran = response()
        print(ran)
        if ran == "Rock":
            print("You WIN")
        else:
            print("TRY AGAIN")
    elif answer == "Scissors":
        ran = response()
        print(ran)
        if ran == "Paper":
            print("You WIN")
        else:
            print("TRY AGAIN")
    else:
        error()


def main():
    intro()
    while True:
        answer = input()
        process_input(answer)


if __name__ == "__main__":
    main()
