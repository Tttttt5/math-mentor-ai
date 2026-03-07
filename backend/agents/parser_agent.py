import re


def detect_operation(text):

    text = text.lower()

    if any(k in text for k in ["derivative", "differentiate", "d/dx"]):
        return "derivative"

    if "limit" in text:
        return "limit"

    if any(k in text for k in ["solve", "equation"]):
        return "solve"

    if "simplify" in text:
        return "simplify"

    if "probability" in text:
        return "probability"

    return "unknown"


def detect_topic(operation):

    if operation in ["derivative", "limit"]:
        return "calculus"

    if operation in ["solve", "simplify"]:
        return "algebra"

    if operation == "probability":
        return "probability"

    return "unknown"


def extract_expression(text):

    text = text.lower()

    match = re.search(r"of\s+(.*)", text)

    if match:
        expr = match.group(1)
    else:
        expr = text

    expr = expr.replace("^", "**")

    return expr.strip()


def extract_variables(text):

    variables = []

    for var in ["x", "y", "z"]:
        if var in text:
            variables.append(var)

    return variables


def parse_problem(text):

    operation = detect_operation(text)

    topic = detect_topic(operation)

    expression = extract_expression(text)

    variables = extract_variables(text)

    needs_clarification = operation == "unknown"

    return {
        "problem_text": text,
        "expression": expression,
        "operation": operation,
        "topic": topic,
        "variables": variables,
        "needs_clarification": needs_clarification
    }