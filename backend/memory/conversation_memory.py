from collections import defaultdict, deque

# Store the last 10 messages per session
_MEMORY = defaultdict(lambda: deque(maxlen=10))


def add_message(session_id: str, role: str, content: str):
    """
    Add a message to the conversation history.

    role: "user" or "assistant"
    """
    _MEMORY[session_id].append({
        "role": role,
        "content": content
    })


def get_history(session_id: str):
    """
    Return the conversation history as a list.
    """
    return list(_MEMORY[session_id])


def clear_history(session_id: str):
    """
    Clear conversation history.
    """
    _MEMORY[session_id].clear()