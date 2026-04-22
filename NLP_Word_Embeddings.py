# Word Embeddings
# Embeddings convert words into numbers in a way that preserves MEANING

# Similar Meaning --> Similar numbers --> Close in Space

# Hospital, Clinic, Airport, Python, JavaScript, Cricket
# Hospital + clinic
# Python + JavaScript

# A Word gets converted into a list of numbers (a vector)

# King and Queen --> numbers are closer
# King and Apple --> numbers are very far

# King = [0.2, 0.9, -0.4, 0.7,....]
# Queen = [0.3, 0.7, -0.2, 0.6,...]
# Apple = [-0.5, 0.1, 0.9, -0.3,..]

# king - man + woman = queen

# King = [0.9, 0.7, 0.2]
# Man = [0.8, 0.1, 0.1]
# Woman = [0.7, 0.1, 0.9]
# Queen = [0.8, 0.7, 1.0]

# Step 1 : Convert Text --> Numbers/embedding vectors
# Step 2 : Compare those vectors using Cosine Similarity
# Step 3 : Find closest vectors = most similar meaning

# How are these embeddings generated

# Sentence --> [Embedding Model] --> Vector of numbers

# Model           Made By             Vector Size
# Word2Vec         Google                300
# GloVe            Stanford              100-300
# sentence-        HuggingFace           384
# transformers
# text-embedding-   OpenAI               1536
# ada-002

# Embeddings working together

# 1. Google Search : Match query meaning, not only on keywords
# 2. ChatGPT / RAG : Find relevant document chunks by meaning
# 3. Spotify : Recommend songs with similar genre
# 4. Swiggy / Zomato : "Biriyani" --> also shows pulao, fried rice
# 5. Netflix : "You liked this movie" --> Similar vibe movies


# Feature                      BOW             TF-IDF       Embeddings

# Word Frequence                Y                Y             Y
# Filters common words          N                Y             Y
# Word Order                    N                N             Y
# Semantic meaning              N                N             Y
# Sparse Vector                 Y                Y             N