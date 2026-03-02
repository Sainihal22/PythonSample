# Sets

# 1. There is no duplicacy.
# 2. Only Unique Values.
# 3. Unordered.
# 4. Mutable.
# 5. Represented by {}

# numbers = {1,2,3,4,5}

# Printing
# numbers = {1,2,3,4,5}
# print(numbers, type(numbers))

# Removing Duplicates
# numbers = {1,1,2,2,3,3,4,4,5,5}
# print(numbers)

# Indexing
# print(numbers[2])  Error
# for num in numbers:
#     print(num)

# Converting
# cities = ['Bangalore',
#  'Hyderabad',
#  'Delhi',
#  'Chennai',
#  'Hyderabad',
#  'Hyderabad',
#  'Hyderabad',
#  'Hyderabad']

# set_city = set(cities)
# print(set_city)

# Adding elements
# numbers.add(6)
# print(numbers)

# Add multiple elements
# numbers.update(["IT", 34, 56.9])
# print(numbers)

# Removing Elements
# numbers.remove(6)

# Safe Removal
# numbers.discard(6)
# print(numbers)

# Pop
# popped_numbers = numbers.pop()
# print(popped_numbers)
# print(numbers)

# Check a value is present or not
# print(7 in numbers) 

# Set Operations
# a = {"IT", "HR"}
# b = {"HR", "Finance"}

# # Union
# print(a | b)

# # Intersection
# print(a & b)

# # Difference
# print(a - b)
# print(b - a)