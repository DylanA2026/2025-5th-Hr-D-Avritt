#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
Rint1 = random.randint(1, 10)
Rint2 = random.randint(1, 10)
Rint3 = random.randint(1, 10)
#4. Print the three variables from #3 on the same line.
print(Rint1, Rint2, Rint3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
RintSum = Rint1 + 2
Rintsub = Rint2 -4
Rintmul = Rint3 * 1.5
#6. Print each result from #5 on the same line.
print(RintSum, Rintsub, Rintmul)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
RandomList = [random.randint(1, 6),
              random.randint(1, 6),
              random.randint(1, 6),
              random.randint(1, 6)]

#8. Sort the list in #7 and print it.
RandomList.sort()
print(RandomList)
#9. Add together the highest three numbers in the list from #7 and print the result.
RandomListSum = RandomList[1] + RandomList[2] + RandomList[3]
print(RandomListSum)
#10. Create a list with 5 names of other students in this class and print the list.
NameList = ['Bill', 'John', 'Bobby', 'Jake','Jack']
print(NameList)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(NameList)
print(NameList)
#12. Print a random choice from the list of names from #10.
print(random.choice(NameList))