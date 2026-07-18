from backend.memory.conversation_memory import *

session = "demo"

add_message(session, "user", "Hello")
add_message(session, "assistant", "Hi!")
add_message(session, "user", "Explain KYC")

print(get_history(session))