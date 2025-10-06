#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW9

import random
#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
numberList = (random.randint(1,100), random.randint(1,100), random.randint(1,100))
#3. Print the list.
print(numberList)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if numberList[0] > numberList[1] and numberList[0] > numberList[2]:
    print(numberList[0], "is the highest number")
    num = numberList[0]
elif numberList[1] > numberList[2] and numberList[1] > numberList[0]:
    print(numberList[1], "is the highest number")
    num = numberList[1]
elif numberList[2] > numberList[0] and numberList[2] > numberList[1]:
    print(numberList[2], "is the highest number")
    num = numberList[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3")
    else:
        print(f"{num} is divisible by 2 but not 3")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 but not 2")
    else:
        print(f"{num} is not divisible by 2 or 3")
