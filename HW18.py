#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads, tails
    totalFlips = heads + tails
    for totalFlips in range(0,101):
        coinFlip = random.randint(0, 1)
        if coinFlip == 0:
            heads += 1
            print(f"Heads: {heads}\nTotal: {totalFlips}")
        else:
            tails += 1
            print(f"Tails: {tails}\nTotal: {totalFlips}")
#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
coin_flip()
#5. Print the final result of heads and tails here
print(f"heads: {heads}\ntails: {tails}")

#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = [
    "red",
    "blue",
    "yellow",
    "green",
    "pink"
    ]

#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def BeanPull(*beanbag):
    chosenBean = random.choice(beanBag)
    print(f"Chosen bean: {chosenBean}")
    beanBag.remove(chosenBean)
    print(f"Remaining beans: {beanBag}")
    replay_beanPull()


#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def replay_beanPull():
    replaying = int(input("Enter 1 to Pull another bean\nEnter 2 to quit\n: "))
    if replaying == 1:
        BeanPull()
    else:
        print("Thank you for playing")
        exit()
#9. Call the "Bean Pull" function here
BeanPull()