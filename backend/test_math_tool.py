from tools.sympy_math_tool import execute_math_tool

expr = "x**2 + 3*x"

result = execute_math_tool(
    "sympy_derivative",
    expr
)

print(result)