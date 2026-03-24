# Bag Of Words (BOW)

# Step 1 : Sentence
# I Love Python

# Step 2

# S1 = "I love Python"
# S2 = "I love Coding"

# Step 3 : Vocabulary
# -> Takes all the unique words
# ["i", "love", "python", "coding"]

# Each word = Each Column

# from sklearn.feature_extraction.text import CountVectorizer

# sentences = [
#     "I love Python",
#     "I love Coding"
# ]

# vectorizer = CountVectorizer()

# x = vectorizer.fit_transform(sentences)

# print(vectorizer.get_feature_names_out())
# print(x.toarray())

# Limitations

# 1. Ignores meaning : like good, bad, negative, positive. It sees everything as a count of words
# 2. Ignores Order : I love Python, Python love I : [1,1,1] = [1,1,1] : in language : order matters
# 3. Too many Zeros (Sparse Data) : [i, love, python, coding, bugs, solve, data, AI]
     # S1 = i love python : [1,1,1,0,0,0,0,0]
    # 1. More memory usage
    # 2. Slower Computation
    # 3. Less efficient model
# 4. What if a sentence is completely unique ?

# S1 = "I love python coding"
# vocub = ["i", "love", "python", "coding", "bugs"]
# S2 = "I love python bugs"
# Vector1 = [1,1,1,0]
# Vector2 = [1,1,0,1]

# TF-IDF
