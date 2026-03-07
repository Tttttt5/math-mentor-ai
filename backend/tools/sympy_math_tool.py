import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

transformations = (
    standard_transformations +
    (implicit_multiplication_application,)
)


def derivative_tool(expression):

    x = sp.symbols("x")

    expr = parse_expr(expression, transformations=transformations)

    result = sp.diff(expr, x)

    return str(result)


def equation_solver_tool(expression):

    x = sp.symbols("x")

    expr = parse_expr(expression, transformations=transformations)

    result = sp.solve(expr, x)

    return str(result)


def simplify_tool(expression):

    expr = parse_expr(expression, transformations=transformations)

    result = sp.simplify(expr)

    return str(result)


def execute_math_tool(strategy, expression):

    if strategy == "derivative":
        return derivative_tool(expression)

    if strategy == "equation":
        return equation_solver_tool(expression)

    if strategy == "simplify":
        return simplify_tool(expression)

    return "Unsupported math operation"