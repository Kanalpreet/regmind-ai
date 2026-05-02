from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pdf_reader import extract_text
import openai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')


def chunk_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def create_vector_db(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings


def retrieve_chunks(query, chunks, index, k=3):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k)

    return [chunks[i] for i in I[0]]


def ask_llm(context, question):
    prompt = f"""
You are a financial compliance expert.

Context:
{context}

Question:
{question}

Provide:
1. Answer
2. Risk Level (High/Medium/Low)
3. Explanation
4. Suggested Action
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    print("\n🚀 Building RegMind AI...\n")

    text = extract_text("data/raw/rbi_kyc.pdf")
    chunks = chunk_text(text)

    index, embeddings = create_vector_db(chunks)

    while True:
        query = input("\n💬 Ask your compliance question: ")

        if query.lower() == "exit":
            break

        relevant_chunks = retrieve_chunks(query, chunks, index)

        context = "\n\n".join(relevant_chunks)

        answer = ask_llm(context, query)

        print("\n🤖 RegMind AI Response:\n")
        print(answer)