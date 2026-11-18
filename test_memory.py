from services.memory_service import MemoryService

memory = MemoryService()

memory.create_user("vijay")

memory.add_message(
    "vijay",
    "user",
    "Hello AI"
)

memory.add_message(
    "vijay",
    "assistant",
    "Hello Vijay!"
)

print(memory.get_history("vijay"))