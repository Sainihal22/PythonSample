# Functions

# 1. User Defined Functions
# 2. In-built Functions

# User Defined Functions

# 1. Declare
# 2. Define
# 3. Always start with a keyword def

# def add():
#     pass

# Normal Functions
# def add():
#     a = 5
#     b = 6
#     c = a + b
#     print(f"The Sum of {a} and {b} is {c}")

# add()

# Parametised Functions
# def add(a,b):
#     c = a+b
#     print(f"The Sum of {a} and {b} is {c}")

# add(4,5)

# Default Parametised Functions
# def add(a = 7, b = 4):
#     c = a + b
#     print(f"The Sum of {a} and {b} is {c}")

# add(1,2)

# Functions with a return Statement

# def add(a,b):
#     c = a + b
#     return c

# added_output = add(6,9)
# # print(added_output)
# print(add(6,9))

# def max_salary(lst):
#     max_salary_var = lst[0]
#     for i in lst:
#         if i > max_salary_var:
#             max_salary_var = i
#     # return max_salary_var
#     print(max_salary_var)


# lst =[12000, 18000, 25000, 8000, 8000, 8000, 8000, 8000]
# print(max_salary(lst))

# Returning Multiple Values

# def add(a,b):
#     c = a + b
#     return c,a,b

# a = 5
# b = 9
# output = add(a,b)
# print(output)

# a,b,c = add(9,8)
# print(f"The Sum of {b} and {c} is {a}")

# Scope
# 1. Global
# 2. Local
# a = 7
# a = 0
# def add():
#     global a
#     a = 9
#     b = 7
#     print(a*b)

# print(a)
# add()
# print(a)

##### Modules ######

from Maths.maths_utils import add, substract

a = 10
b = 5
print(add(a,b))
print(substract(a,b))