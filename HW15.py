#Name:
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
d = a + b
e = d /c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(e)
if e % 2 == 0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
randomList = [
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10)]

#7. Print the 4th number in the list.
print(randomList[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randomList.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randomList.sort()
print(randomList[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 101:
    print(i)
    i = i + 1

#11. Create a list containing the names of five other students in the classroom.
students = [
    "Ivan",
    "Sam",
    "Aidan",
    "Jude",
    "Brenlen"
]
#12. Create a for loop that individually prints out the names of each student in the list.
for s in students:
    print(s)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for t in range(1,101):
    if t % 10 == 0:
        break
    else:
        print(t)
#14. Free space. Do something creative. :)

RandomNumber = random.randint(1, 10)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 10.")

attempts = 0
while attempts < 3:
    numberGuessed = (int(input("Guess a number between 1 and 10: ")))

    if numberGuessed < RandomNumber:
        print("Too low. Try Again")
        attempts += 1

    elif numberGuessed > RandomNumber:
        print("Too high. Try Again")
        attempts += 1

    else:
        print("You got it right!")
        break


print(f"Thank you for playing! I guessed the number was {RandomNumber}")