import os

from groq import Groq
from dotenv import load_dotenv

from backend.config import GROQ_MODEL

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GROQ CLIENT
# =========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================================
# QUESTION REWRITER
# =========================================

def rewrite_question(conversation_history, current_question):

    if not conversation_history:
        return current_question

    history = ""

    for message in conversation_history:
        history += f"{message['role'].capitalize()}: {message['content']}\n"

    prompt = f"""
You are a query rewriting assistant for an RBI compliance RAG system.

Your job is to rewrite the user's latest question into a COMPLETE, STANDALONE question using the previous conversation.

Rules:

- Preserve the original meaning.
- Resolve references like:
  - it
  - they
  - this
  - those
  - what about
  - and for...
- Do NOT answer the question.
- Do NOT add new facts.
- Return ONLY the rewritten question.

====================================
Conversation
====================================

{history}

====================================
Current User Question
====================================

{current_question}

====================================
Standalone Question
====================================
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    rewritten_question = response.choices[0].message.content.strip()

    return rewritten_question 