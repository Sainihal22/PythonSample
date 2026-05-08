# # Install required library
# pip install sentence-transformers

# list of pre trained models under SentenceTransformer

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a pre-trained model

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully")

def semantic_search(query, documents, model, top_k=3, threshold_value = 0.5):
    """
    Given a query, find the most semantically similar documents.
    """

    # Step 1: Embed the query
    query_vector = model.encode([query])

    # Step 2: Embed all documents
    doc_vectors = model.encode(documents)

    # Step 3: Calculate cosine similarity
    scores = cosine_similarity(query_vector, doc_vectors)[0]

    # Step 4: Rank by score
    ranked_indices = np.argsort(scores)[::-1][:top_k]

    # Step 5: Return results
    print(f"\n🔍 Query: '{query}'")
    print(f"{'─'*50}")
    print(f"Top {top_k} Results:\n")

    found = False

    for idx in ranked_indices[:top_k]:

        print(f"{documents[idx]} --> {scores[idx]}")

        if scores[idx] >= threshold_value:
            found = True
            print(f"\n Scores : {scores[idx]}")
            print(f"--> {documents[idx]}")
    
    if not found:
        print("\n No relevant documents found")

    # for rank, idx in enumerate(ranked_indices, 1):
    #     print(f"  Rank {rank} [Score: {scores[idx]:.2f}]")
    #     print(f"  → {documents[idx]}")
    #     print()

    

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

# embeddings = model.encode(documents)

# print(f"Number of Documents : {len(documents)}")
# print(f"Embedding Shape : {embeddings.shape}")
# print(f"One Vector (first 5 values) : {embeddings[0][:5]}")

semantic_search("Python Web Development", documents, model)
# semantic_search("cricket players and tournaments", documents, model)
# semantic_search("how AI learns", documents, model)
# semantic_search("What is dell Technologies ?", documents, model)