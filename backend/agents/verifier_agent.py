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


def verify_solution(expression, solution, operation="derivative"):

    result = {
        "verified": False,
        "confidence": 0.0
    }

    try:

        x = sp.symbols("x")

        expr = parse_expr(expression, transformations=transformations)

        predicted = parse_expr(solution, transformations=transformations)

        if operation == "derivative":

            correct = sp.diff(expr, x)

            if sp.simplify(correct - predicted) == 0:
                result["verified"] = True
                result["confidence"] = 0.95
            else:
                result["confidence"] = 0.3

    except Exception:

        result["confidence"] = 0.1

    return result