#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
NameList = ["Billy", "John", "Joe", "Johny", "Bobby"]
#2. Append a new name onto the Name List.
NameList.append("Steve")
#3. Print out the 4th name on the list.
print(NameList[3])
#4. Create a list with 4 different integers in it.
NumList = [18, 21, 3, 42]
#5. Insert a new integer into the 2nd spot and print the new list.
NumList.insert(1, 5)
print(NumList)
#6. Sort the list from lowest to highest and print the sorted list.
NumList.sort()
print(NumList)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numListSum = NumList[0] + NumList[1] + NumList[2]
print(numListSum)
#8. Create a list with two strings, two variables, and too boolean values.
MixedList = ["Billy", "mechanic", 41, 4, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(MixedList[int(input("Enter Index Value: "))])
