#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
EmptyList = [

]
#3. Create a list that contains the names of everyone in the classroom.
Class = [
    "Dylan",
    "Bryson",
    "Aiden",
    "Ivan",
    "Ashton",
    "Hogan",
    "Brennlyn",
    "Sam"
     ]

#4. Print the list from #3, sort the list, then print the list again.
print(Class)
Class.sort()
print(Class)
#5. Append 5 different integers into the empty list from #2 and print the list.
EmptyList.append(6)
EmptyList.append(7)
EmptyList.append(6)
EmptyList.append(9)
EmptyList.append(2)
print(EmptyList)
#6. Add together the middle three numbers in the list from #2 and print the result.
sumlist = EmptyList[1] + EmptyList[2] + EmptyList[3]
print(sumlist)
#7. Remove the very first number in the list from #2. Print the new first number.
EmptyList.pop(0)
print(EmptyList[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
Me= {
    "Name": "Dylan",
    "Grade": 12,
    "Color": "Red"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
Me.update({"Candy" : "Kitkat"})

#10. Print ONLY the values of the dictionary from #8.
print(Me.values())