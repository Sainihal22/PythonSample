from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Knowledge base
# documents = [
#     "python is used for machine learning",
#     "cricket is popular in India",
#     "FastAPI is a python web framework",
#     "Virat Kohli plays cricket",
#     "python is great for data science"
# ]

documents = [
    "Python is used for machine learning",
    "Cricket is the most loved sport in India",
    "FastAPI is a modern Python web framework",
    "Virat Kohli is a famous cricket player",
    "Neural networks are inspired by the human brain",
    "Django and Flask are Python frameworks",
    "IPL is a cricket tournament",
    "Deep learning uses multiple layers of neurons"
]

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def tfidf_search(query, documents, vectorizer, doc_vectors, top_k=3):
    # Convert query to TF-IDF vector
    query_vector = vectorizer.transform([query])

    # Cosine similarity
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    print(scores)

    # Rank results
    ranked = np.argsort(scores)[::-1][:top_k]
    print(ranked)

    print(f"\n🔍 Query: '{query}'")
    print("─" * 45)
    for rank, idx in enumerate(ranked, 1):
        print(f"  Rank {rank} [Score: {scores[idx]:.2f}] → {documents[idx]}")

# tfidf_search("Python Web Development", documents, vectorizer, doc_vectors)
# tfidf_search("cricket players and tournaments",     documents, vectorizer, doc_vectors)
tfidf_search("how AI learns",     documents, vectorizer, doc_vectors)
# tfidf_search("cricket sports",     documents, vectorizer, doc_vectors)
