#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import hello_world,average,animal_list,loop
#2. Call the functions here and run HW19
hello_world()
average(1, 2, 3)
animal_list("cat", "dog", "monkey", "mouse", "rabbit")
loop(int(input("Enter number to loop: ")))
#3. Delete all calls from HW16 and run HW19 again.


#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    number = int(input("Give me an integer"))
    print(number)
except:
    raise ValueError("It needs to be an integer!")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
j = 5
while j >= 0:
    print(j)
    j -= 1
raise Exception("You can't count below zero!")
