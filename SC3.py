#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

x = 0

while True:
    players = int(input("Insert the number of players: ? "))
    if players <= 1:
        print("You must have more than 1 player")
        continue
    count = players
    while not players == 0:
        score = int(input("Insert the score between 1 and 5: "))
        if score > 5 or score < 1:
            print("Score must be between 1 and 5")
            continue
        players -= 1
        x += score
        print(f"The score is {score}.")

    y = x / count
    print(f"The average score is {y}.")

