print ("Welcome, please type: rock, paper or scissors to play, enjoy!")
import random

final1= ("rock", "paper", "scissors")
final= (random.choice(final1))

while True:
    secim = input (">")

    if secim == final:
        print ("Opponent choosen", final)
        print ("Draw!")
        break
    elif secim == "rock" and final == "paper":
        print("Opponent choosen", final)
        print ("You lost!")
        break
    elif secim == "rock" and final == "scissors":
        print("Opponent choosen", final)
        print("You won!")
        break
    elif secim == "scissors" and final == "rock":
        print("Opponent choosen", final)
        print("You lost!")
        break
    elif secim == "scissors" and final == "paper":
        print("Opponent choosen", final)
        print("You won!")
        break
    elif secim == "paper" and final == "scissors":
        print("Opponent choosen", final)
        print("You lost!")
        break
    elif secim == "paper" and final == "rock":
        print("Opponent choosen", final)
        print("You won!")
        break
    else:
        print ("Please type rock, paper or scissors")

input("Press enter to quit")
exit()
