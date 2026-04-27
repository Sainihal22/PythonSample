# Word2Vec

# Two Approaches

# Approach 1 : CBOW
# Approach 2 : Skip-gram

# Approach 1
# CBOW (Continuous Bag of Words)
# Given the surrounding words --> predict the middle word

# I drink ___________ every morning

# Approach 2
# Skip-gram
# Given one word --> predict the surrounding words

# Coffee

# CBOW : The neighbours help you guess the word,
# Skip-gram : The word helps you guess the neighbours..

# Both teach the model about relationships....

# Learning Step by Step

# Sentence 1 : "dog eats food"
# Sentence 2 : "cat eats food"
# Sentence 3 : "dog and cat are pets"

# 1. Sliding Window
# The model slides a window across every sentnce : 

# Window Size = 1 (one neigbbour each side)

# "dog eats food"
# --> (eats --> dog), (eats --> food)

# "cat eats food"
# --> (eats --> cat), (eats --> food)

# Step 2 : The Model sees a pattern

# "dog" appears near : eats, pet
# "cat" appears near : eats, pet

# --> Model concludes : dog and cat are SIMILAR
# --> Their Vectors get pulled CLOSER together

# Step 3 : Vectors get adjusted
# Think of it like a magnet system : 

# Before training : 
# "dog" --> [0.1, 0.9, 0.2] (random)
# "cat" --> [0.8, 0.1, 0.5] (random, far way)

# After training on similar contexts : 
# "dog" --> [0.7, 0.6, 0.4]
# "cat" --> [0.6, 0.7, 0.3]  <-- Pulled closer !

# Word2Vec --> It gives vectors per word.
# Averaging loss of words for order and context

# Ex : 

# "I Love Python" --> [vec(I) + vec(Love) + vec(Python)] / 3
#                 --> Avg of words

# TRANSFORMERS (BERT)

# There is a big snake near a river bank
# There is a lot of money in the bank

# BERT reads whole sentence at one : 
# --> Understands the context
# "bank" near "river" =! "bank" near "money"
# produces one rich vector for the full sentence

# Raw Text
#    ↓
# Preprocessing (lowercase, remove punctuation, stopwords)
#    ↓
# BoW → counts words (no meaning)
#    ↓
# TF-IDF → weights important words (no meaning)
#    ↓
# Word2Vec → words get meaning via context
#    ↓
# Sentence Transformers → full sentences get meaning
#    ↓
# Vector → Cosine Similarity → Search → RAG → ChatGPT