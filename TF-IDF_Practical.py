# Manually
# documents = [
#     "I love python",
#     "I love coding",
#     "I love AI"
# ]

# # Part 1 : Building TF-IDF from Scratch

# # Step 1 : Tokenize

# # Split each document into words
# tokenized = [doc.lower().split() for doc in documents]

# print(tokenized)

# # Step 2 : Build Vocabulary

# # All unique words across all documents
# vocab = sorted(set(word for doc in tokenized for word in doc))

# print("Vocabulary:", vocab)

# # Step 3 : Calculate TF

# def compute_tf(tokenized_doc):
#     tf = {}
#     total_words = len(tokenized_doc)

#     for word in tokenized_doc:
#         tf[word] = tf.get(word, 0) + 1

#     # Divide by total words
#     for word in tf:
#         tf[word] = tf[word] / total_words

#     return tf

# # Compute TF for all documents
# # tf_scores = [compute_tf(doc) for doc in tokenized]
# tf_scores = []
# for doc in tokenized:
#     tf_scores.append(compute_tf(doc))

# # Show results
# for i, tf in enumerate(tf_scores):
#     print(f"\nDoc {i+1} TF: {tf}")

# # Calculate IDF
# import math

# def compute_idf(tokenized_docs, vocab):
#     total_docs = len(tokenized_docs)
#     idf = {}

#     for word in vocab:
#         # Count how many docs contain this word
#         doc_count = sum(1 for doc in tokenized_docs if word in doc)

#         # IDF formula
#         idf[word] = math.log(total_docs / doc_count)

#     return idf

# idf_scores = compute_idf(tokenized, vocab)

# print("\nIDF Scores:")
# for word, score in idf_scores.items():
#     print(f"  {word:10s} → {score:.4f}")

# # Calculate TF-IDF

# def compute_tfidf(tf_scores, idf_scores, vocab):
#     tfidf_matrix = []

#     for tf in tf_scores:
#         tfidf_row = []
#         for word in vocab:
#             tf_val  = tf.get(word, 0)
#             idf_val = idf_scores[word]
#             tfidf_row.append(round(tf_val * idf_val, 4))
#         tfidf_matrix.append(tfidf_row)

#     return tfidf_matrix

# tfidf_matrix = compute_tfidf(tf_scores, idf_scores, vocab)

# # Display nicely
# print(f"\n{'Word':<10}", end="")
# for word in vocab:
#     print(f"{word:>10}", end="")
# print()

# for i, row in enumerate(tfidf_matrix):
#     print(f"Doc {i+1}    ", end="")
#     for val in row:
#         print(f"{val:>10.4f}", end="")
#     print()

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "I love python",
    "I love coding",
    "I love AI"
]

# Create a vectorizer
vectorizer = TfidfVectorizer()
# Object Creation, what will this do : 
# 1. Break sentences into words (tokens)
# 2. Removes common stopwords (like "I" automatically ignored)
# 3. Computes TF-IDF Scores

# Fit and Transform
tfidf_matrix = vectorizer.fit_transform(documents)
# It does two things : 
# Fit : Learns all unique words (vocabulary)
# Transform : Converts each sentence into a numerical vector

# Get Feature Names
vocab = vectorizer.get_feature_names_out()
# This will give column names

df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns = vocab,
    index=["Doc1", "Doc2", "Doc3"]
)

print(df)