from agents.router_agent import route_problem

parsed_problem = {
    "problem_text": "Find derivative of x^2 + 3x",
    "topic": "calculus",
    "operation": "derivative",
    "variables": ["x"],
    "constraints": [],
    "needs_clarification": False
}

route = route_problem(parsed_problem)

print("\nRouting Decision:\n")
print(route)