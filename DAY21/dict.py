# key- value pair --->hash map
student ={"name": "nihal", "age": 20, "marks": 90, "is_pass": True}
print(student ["name"])

# access the key with doesnt exist
# print(student["address"]) # KeyError: 'address

print(student.get("name"))

# update the value
student["marks"] = 95
print(student)
# add new key value pair
student["address"] = "Bangalore"
print(student)
# delete the key value pair
del student["is_pass"]
print(student)
# check if key exists
print("name" in student)  # True
print("is_pass" in student)  # False
# iterate over keys
for key in student:
    print(key, student[key])
# iterate over items
for key, value in student.items():
    print(key, value)
# iterate over values
for value in student.values():
    print(value)
# clear the dictionary
student.clear()
print(student)  # {}
# copy the dictionary
student_copy = student.copy()
print(student_copy)  # {}
