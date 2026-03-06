# Numpy
# Numerical Python : Fast Numerical computations

# numbers = [1,2,3,4,5]

# # Output : [2,4,6,8,10]

# numbers2 = []

# for num in numbers:
#     numbers2.append(2 * num)

# print(numbers2)

# ARRAY

import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr * 2)

# 1D Array : Vector
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr)) # to get type
# print(arr.shape) # to get structure of an array

# 2D Array : Matrix
# matrix = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# 3D Array : Matrix
# arr3d = np.array([
#     [[1,2], [3,4]],
#     [[5,6], [7,8]]
# ])

# print(arr3d)
# print(arr3d.shape)
# print(arr3d.ndim)

# Built in Array Creation

# print(np.zeros((2,3)))
# print(np.ones((3,3)))
# print(np.arange(0,10))
# print(np.linspace(0,1,5))

# arr = np.array([1,2,3,4,5])

# Indexing and Slicing

# 1D
# print(arr[2])
# print(arr[2:5])

# 2D
# matrix = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(matrix)
# print(matrix[0,1])
# print(matrix[1:])
# print(matrix[:2])