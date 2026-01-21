from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama

from rag import retrieve_context

app = FastAPI()

llm = Ollama(model="llama3")

class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
def chat(request: QueryRequest):
    context = retrieve_context(request.query)

    prompt = f"""
    You are an enterprise AI assistant.
    Use the context below to answer accurately.

    Context:
    {context}

    Question:
    {request.query}
    """

    response = llm.invoke(prompt)
    return {"answer": response}
