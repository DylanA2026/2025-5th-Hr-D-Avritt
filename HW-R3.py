#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print("Hello World!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
print(a, b, c)
#3. Create a list containing 5 strings listing 5 colors.
colors = ['red', 'blue', 'green', 'yellow', 'pink']
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
pickedcolor = random.choice(colors)
print(pickedcolor)
#5. Create an if statement that determines which of the three variables from #2 is the lowest.

############################################
### Check to see which ones are the same ###
############################################
if a == b and a < c:
    print("A and B are the lowest")
elif b == c and b < a:
     print("B and C are the Lowest")
elif a == c and a < b:
    print("A and C are the Lowest")


elif c > a < b:
    print(f"A is the lowest number {a}")
elif c > b < a :
    print(f"B is the lowest number {b}")
else:
    print(f"C is the lowest number {c}")