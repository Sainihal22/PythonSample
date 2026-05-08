# Why Vector DB
# Problems : 

# 1. Server restarts --> everything gone
# 2. 1 million documents --> RAM explodes
# 3. No way to update one document
# 4. Search = compare with EVERY vector = slow

# Normal DB vs Vector DB

# Feature       NormalDB                 VectorDB
# Stores        Rows and Columns         Vectors (list of numbers)
# Search        Exact Match              Meaning / Similarity
# Query         Where name = "Python"    find similar to [0.2, 0.03, 0.8, ....]
# Use Case      User data, Orders        Semantic search, RAG
# Example       PostgreSQL, MYSQL        ChromaDB, Pinecone, FAISS, PGVector

# ChromaDB
# 1. Runs locally (No need to Internet, No need of API key)
# 2. Pure Python
# 3. Stores on Disk
# 4. Built for RAG
# 5. Free

# ChromaDB
# 1. Client --> Connection to ChromaDB (like DB connection)
# 2. Collection --> A group of related documents (like a table)
# 3. Documents --> The actual text
# 4. Embeddings --> Vectors for each document
# 5. IDs --> Unique identifier for each document

# Analogy
# 1. Client = Opening a db connection
# 2. Collection = A Table in that DB
# 3. Documents = row
# 4. Embeddings = A special indexed column
# 5. IDs = Primary Key

# pip install chromadb
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding Model loaded")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="/.my_vectordb")
# PersistentClient --> Datra is saved into the folder, Even if server restarts - data is still there
print("ChromaDB Connected")

# Create a collection
collection = client.get_or_create_collection(
    name = "students_knowledge_base"
)
print("Collection is ready")
print(f"Documents in collection : {collection.count()}")

# documents = [
#     "Python is a programming language used for AI and machine learning",
#     "FastAPI is a modern Python web framework for building APIs",
#     "Machine learning is a subset of artificial intelligence",
#     "Deep learning uses neural networks with multiple layers",
#     "Cricket is the most popular sport in India",
#     "Virat Kohli is a famous Indian cricket player",
#     "IPL is a professional cricket tournament held in India",
#     "NumPy is a Python library for numerical computing",
#     "Pandas is used for data manipulation and analysis in Python",
#     "Vector databases store embeddings for semantic search",
#     "RAG stands for Retrieval Augmented Generation",
#     "Embeddings convert text into numerical vectors",
#     "Cosine similarity measures the angle between two vectors",
#     "TF-IDF stands for Term Frequency Inverse Document Frequency",
#     "Transformers are deep learning models used in NLP",
# ]

# print("Generating embeddings....")
# embeddings = model.encode(documents).tolist()
# print(f"Generated {len(embeddings)} embeddings")

# # Create unique IDs
# ids = [f"doc_{i}" for i in range(len(documents))]

# # Add to chromadb
# collection.add(
#     documents = documents,
#     embeddings= embeddings,
#     ids = ids
# )

# print(f"Added {len(documents)} documents")
# print(f"Total in collection : {collection.count()}")

def search(query, collection, model, top_k=3):
    """Search the vector DB by meaning"""

    # Step 1: Embed the query
    query_embedding = model.encode([query]).tolist()

    # Step 2: Search ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    # Step 3: Display results
    print(f"\n{'='*55}")
    print(f"🔍 Query: '{query}'")
    print(f"{'='*55}")

    for i, (doc, distance) in enumerate(zip(
        results['documents'][0],
        results['distances'][0]
    )):
        similarity = 1 - distance   # convert distance to similarity
        print(f"\n  Rank {i+1} [Score: {similarity:.4f}]")
        print(f"  → {doc}")

    return results['documents'][0]

# ── Run searches ──
search("how does AI learn",          collection, model)
search("python libraries for data",  collection, model)
search("cricket tournaments India",  collection, model)
search("how do vectors work in NLP", collection, model)