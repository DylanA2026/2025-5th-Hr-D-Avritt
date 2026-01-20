#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW17

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random


def replay_rps():
    replaying = int(input("Enter 1 to replay rps\nEnter 2 to exit rps\n: "))
    if replaying == 1:
        rps()
    else:
        print("Thank you for playing")
        exit()


def rps():
    players_hand = int(input("1 for Rock\n2 for Paper\n3 for Scissors "))
    opponents_hand = random.randint(1,3)

# Establish Oppenents Hand
    if opponents_hand == 1:
        opp_Hand = "Rock"
    elif opponents_hand == 2:
        opp_Hand = "Paper"
    else:
        opp_Hand = "Scissors"
    print(f"Opponent picked {opp_Hand}.")

    if players_hand == opponents_hand:
        print("Draw")
#Lose statements
    elif players_hand == 1 and opponents_hand == 2:
        print("You chose Rock and opponent picked Paper! You Lose")

    elif players_hand == 2 and opponents_hand == 3:
        print("You chose Paper and opponent picked Scissors! You Lose")

    elif players_hand == 3 and opponents_hand == 1:
        print("You chose Scissors and opponent picked Rock! You Lose")
#Win Statements

    elif players_hand == 1 and opponents_hand == 3:
        print("You chose Rock and opponent picked Scissors! You Win!")

    elif players_hand == 2 and opponents_hand == 1:
        print("You chose Paper and opponent picked Rock! You Win!")

    elif players_hand == 3 and opponents_hand == 2:
        print("You chose Scissors and opponent picked Paper! You Win!")

    replay_rps()


rps()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

