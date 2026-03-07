import re

from tools.sympy_math_tool import execute_math_tool
from rag.retriever import retrieve_context


def normalize_expression(expr):

    expr = expr.lower()

    # remove accidental flags
    expr = expr.replace(",false", "")
    expr = expr.replace(",true", "")

    # convert power syntax
    expr = expr.replace("^", "**")

    expr = expr.replace("squared", "**2")
    expr = expr.replace("cubed", "**3")

    expr = expr.replace(" ", "")

    return expr


def extract_expression(problem_text):

    text = problem_text.lower()

    # derivative of ...
    match = re.search(r"of\s+(.*)", text)

    if match:

        expr = match.group(1)

    else:

        # solve ...
        match = re.search(r"solve\s+(.*)", text)

        if match:

            expr = match.group(1)

        else:

            expr = text

    expr = normalize_expression(expr)

    return expr


def solve_problem(parsed_problem, route):

    problem_text = parsed_problem["problem_text"]

    strategy = route["solver_strategy"]

    use_rag = route.get("use_rag", False)

    # Extract expression safely
    expression = extract_expression(problem_text)

    rag_context = []

    if use_rag:

        rag_context = retrieve_context(problem_text)

    try:

        solution = execute_math_tool(strategy, expression)

    except Exception:

        solution = "Solver error"

    return {

        "expression": expression,

        "solution": solution,

        "rag_context": rag_context

    }