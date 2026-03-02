# Dictionary

# 1. Unordered.
# 2. Traversing
# 3. Mutable
# 4. Key-value pairs
# 5. Represented by : {}

student = {
    "34" : {"Name" : "Nihal","Age" : 25},
    "56" : {"Name" : "Arjun","Age" : 24},
    "Shruti" : [12345678, 456799101]
}

# Printing
# print(student)
# print(type(student))

# Indexing
# print(student["34"]["Name"])
# print(student["Shruti"])

# Printing Keys
# print(student.keys())

# Printing Values
# print(student.values())

# Traversing
# for key, value in student.items():
#     print(key, value)
# print(student.items())

# Updating values
# student["34"] = {
#     "Name" : "Subhash","Age" : 28
# }
# print(student)

# Adding a data into dict
# student["40"] = {
#     "Name" : "Priya", "Age": 26
# }
# print(student)

# Delete/Remove a data from dict
# student.pop("34")
# print(student)

# student.pop("30")
# print(student)

# del student["34"]
# print(student)

# Renaming a key
# student["32"] = student.pop("34")
# print(student)