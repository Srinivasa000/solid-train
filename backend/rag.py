import os
from dotenv import load_dotenv
from pinecone import Pinecone
from embeddings import get_embedding

load_dotenv()

# Create Pinecone client
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

# Connect to existing index
index = pc.Index(os.getenv("PINECONE_INDEX"))

def retrieve_context(query: str, top_k: int = 3):
    query_embedding = get_embedding(query)

    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    contexts = []
    for match in results["matches"]:
        if "text" in match["metadata"]:
            contexts.append(match["metadata"]["text"])

    return "\n".join(contexts)
