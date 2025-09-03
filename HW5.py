#Name:
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
NumList = [81, 21, 33, 4, 54, 6, 47, 18, 69]
#2. Sort the list from highest to lowest.
NumList.sort(reverse=True)
#3. Create an empty list.
EmptyList = []
#4. Remove the median number from the first list and add it to the second list.
EmptyList.append(NumList[4])
NumList.pop(4)
#5. Remove the first number from the first list and add it to the second list.
EmptyList.append(NumList[0])
NumList.pop(0)
#6. Print both lists.
print(NumList)
print(EmptyList)
#7. Add the two numbers in the second list together and print the result.
print(EmptyList[0] + EmptyList[1])
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
NumList.append(EmptyList[1])
EmptyList.pop(1)
#5. Remove the first number from the first list and add it to the second list.
NumList.append(EmptyList[0])
EmptyList.pop(0)
#9. Sort the first list from lowest to highest and print it.
NumList.sort()
print(NumList)