import random

RandomNumber = random.randint(1, 10)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")
numberGuessed = (int(input("Guess a number between 1 and 100: ")))

attempts = 0
while True:
    try:
        numberGuessed = (int(input("Guess a number between 1 and 100: ")))
        attempts += 1

        if numberGuessed < RandomNumber:print("Too low. Try Again")
        elif numberGuessed > RandomNumber:print("Too high. Try Again")


        else:
          print("You got it right!")
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"Thank you for playing! I guessed the number was {RandomNumber}")
