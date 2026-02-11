#Name: Dylan Avritt
#Class: 5th Hour
#Assigment: SC4
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (SC5) and print the average.
statList = []
# Roll 4 d6 dice
def char_stats():
    diceRoll = [
        random.randint(1,6),
        random.randint(1,6),
        random.randint(1,6),
        random.randint(1,6),
    ]

#Sort from hightest to lowest
    diceRoll.sort(reverse=True)

# add 3 highest together
    statTotal = diceRoll[0]+diceRoll[1]+diceRoll[2]

    statList.append(statTotal)

#run function 5 more times (6 total) and print all stats from list

for _ in range(6):
    char_stats()
print(statList)




