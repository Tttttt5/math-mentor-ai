import os
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-r1:7b")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_store")
MEMORY_DB = os.getenv("MEMORY_DB", "memory.db")