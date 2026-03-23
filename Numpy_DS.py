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

# Random

import numpy as np

# 1. Randomly generate Float Numbers between 0 and 1
# click_probability = np.random.rand(1000000)
# click_rate = (click_probability > 0.6)
# print((click_probability > 0.85).mean())

# print(1000000 * 0.150484)

# 2. Randomly generate int values within a range
# print(np.random.randint(6))

# 3. Random Matrix
# print(np.random.rand(3,3))

# 4. Random Choice
# students = ["Amit", "Priya", "Sowmya", "Neha"]
# print(np.random.choice(students, 1))

# Vectors

# v1 = np.array([1,2,3])
# v2 = np.array([4,5,6])

# Operations

# 1. Addition

# v3 = v1 + v2

# print(v3)

# 2. Substraction

# v3 = v1 - v2
# print(v3)

# 3. Scaling

# v3 = v1 * v2
# print(v3)

# Dot Product
# v1 = np.array([1,2,3])
# v2 = np.array([4,5,6])

# v3 = np.dot(v1,v2)
# print(v3)

# Cosine Similarity
# from numpy.linalg import norm

# cos_sim = np.dot(v1,v2) / (norm(v1) * norm(v2))


# import sqlite3

# conn = sqlite3.connect("documents.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS docs (
#     id INTEGER PRIMARY KEY,
#     text TEXT,
#     v1 REAL,
#     v2 REAL,
#     v3 REAL
# )
# """)


# conn = sqlite3.connect("documents.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS docs (
#     id INTEGER PRIMARY KEY,
#     text TEXT,
#     v1 REAL,
#     v2 REAL,
#     v3 REAL
# )
# """)

# data = [
#     ("Learn Python programming", 1, 0, 1),
#     ("Deep learning tutorial", 0, 1, 0),
#     ("FastAPI deployment guide", 1, 1, 1)
# ]

# cursor.executemany("INSERT INTO docs (text, v1, v2, v3) VALUES (?, ?, ?, ?)", data)
# conn.commit()

# cursor.execute("SELECT text, v1, v2, v3 FROM docs")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# import numpy as np
# from numpy.linalg import norm

# def cosine_similarity(a, b):
#     return np.dot(a, b) / (norm(a) * norm(b))

# query = np.array([1, 0, 1])  # simulate embedding of user query

# best_doc = None
# best_score = -1

# for row in rows:
#     text = row[0]
#     vec = np.array(row[1:])

#     score = cosine_similarity(query, vec)

#     print(f"{text} → {score}")
#     print()

#     if score > best_score:
#         best_score = score
#         best_doc = text

# print("\nBest Match:", best_doc)