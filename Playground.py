import random

RandomNumber = random.randint(1, 100)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")
numberGuessed = (int(input("Guess a number between 1 and 100: ")))

attempts = 0

attempts += 1
if numberGuessed < RandomNumber:"Too low"
elif numberGuessed > RandomNumber:"Too high"
else:
    print("You got it right!")

if attempts == 3: print("Sorry you ran out of attempts!")
print("Thank you for playing!")
print(RandomNumber)



