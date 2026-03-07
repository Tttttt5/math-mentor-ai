from graph.agent_graph import math_graph


input_state = {
    "question": "Find derivative of x^2 + 3x"
}

result = math_graph.invoke(input_state)

print("\nGraph Output:\n")

print(result)