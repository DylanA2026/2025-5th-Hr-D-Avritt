#Name:
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
keydictionary = {
"name" : "John",
"age" : [19,27,34],
"job" : True,
}
#3. Print the keys of the dictionary from #2.
print(keydictionary.keys())
#4. Print the values of the dictionary from #2
print(keydictionary.values())
#5. Print one of the three numbers from the list by itself
print(keydictionary["age"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
keydictionary.update({"name" : "Jimmy"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(keydictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
fifth_hour_class = {
    "student_1" : {
        "Name" : "Ivan",
        "Grade" : 12,
        "Sports" : False
    },
    "student_2" : {
        "Name" : "Dylan",
        "Grade" : 12,
        "Sports" : False
    },
    "student_3" : {
        "Name" : "Sam",
        "Grade" : 10,
        "Sports" : False
    },
}

#9. Print the names of all three classmates on the same line.
print(fifth_hour_class["student_1"]["Name"],fifth_hour_class["student_2"]["Name"],fifth_hour_class["student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
fifth_hour_class["student_1"].pop("Sports")
print(fifth_hour_class)
