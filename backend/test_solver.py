from agents.solver_agent import solve_problem

parsed_problem = {
 "problem_text": "Find derivative of x^2 + 3x",
 "topic": "calculus",
 "operation": "derivative"
}

route = {
 "solver_strategy": "sympy_derivative",
 "use_rag": False
}

result = solve_problem(parsed_problem, route)

print("\nSolver Result:\n")
print(result)