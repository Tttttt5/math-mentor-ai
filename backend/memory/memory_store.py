import json
import os

MEMORY_FILE = "memory/problems.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):

    os.makedirs("memory", exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def store_problem(question, solution):

    memory = load_memory()

    memory.append({
        "question": question,
        "solution": solution,
        "source": "model"
    })

    save_memory(memory)


def store_corrected_solution(question, corrected_solution):

    memory = load_memory()

    memory.append({
        "question": question,
        "solution": corrected_solution,
        "source": "human_feedback"
    })

    save_memory(memory)


def get_all_problems():

    memory = load_memory()

    return [(m["question"], m["solution"]) for m in memory]