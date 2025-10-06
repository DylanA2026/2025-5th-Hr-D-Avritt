#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW8

import random
#1. Print "Hello World!"
print("Hello World!")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
#3. Print A, B, and C on the same line.
print(a, b, c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a > 5:
    print("A is greater than 5")
elif a < 5:
        print("A is less than 5")
else:
        print("A is equal to 5")

#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if b > 3 and b < 7:
    print("B is greater than 3")
    print("B is less than 7")
else :
    print("B is not between 3 and 7")

#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print("C is even")
else:
    print("C is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
d = random.randint(1,20) + 3
print(d)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if d > a+b+c:
    print("D is greater than A+B+C")
elif d < a+b+c:
    print("D is less than A+B+C")
else:
    print("D is equal to A+B+C")