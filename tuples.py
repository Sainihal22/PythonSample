# tuples

# 1. It is immutable
# 2. Can store mixed data types
# 3. Reading the data, DOB
# t = (22, 12, 1998)

tuple_data = (1,2,3,4)
# print(type(tuple_data))

# for t in tuple_data:
#     print(t)

tuple_list = list(tuple_data)
print(tuple_list)

converted_tuple = tuple(tuple_list)
print(converted_tuple)

tuple_data = (3,7,8,1,5,9,4,1,8)

print(tuple_data.count(8))


# Q. There is a tuple = (3,7,8,1,5,9), but this tuple output be as (3,7,8,1,5,9,4,1,8)

# Q. I have a string = 'Python is a good programming language', string ouput should be 'Python is a programming language'

string = 'Python is a good programming language'
print(string.split())
