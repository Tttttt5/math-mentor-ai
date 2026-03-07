import ollama

LLM_MODEL = "phi3"

def generate_response(prompt):

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]