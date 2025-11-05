#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW12
import time
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    time.sleep(0.4)
    i -= 1
else:
    print("Hello World")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
L = 1
while  L < 30:

    if L % 2 == 0:
        print(L)
        L += 1

    else: L += 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
J = 1
while J < 30:
    if J % 3 == 0:
        J += 1
        continue
    else:
        print(J)
        J += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
print("Step #4")
while True:
    Rd = random.randint(1, 6)
    print(Rd)
    if Rd == 1:
        break
    print(Rd)




#5. Create a while loop that asks for a number input until the user inputs the number 0.
while True:
    if int(input("Enter a number (0 to quit): ")) == 0:
        break
print("Thank you for playing")