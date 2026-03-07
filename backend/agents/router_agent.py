def route_problem(parsed_problem: dict):

    topic = parsed_problem.get("topic", "").lower()
    operation = parsed_problem.get("operation", "").lower()

    route = {
        "solver_strategy": None,
        "use_rag": False,
        "needs_hitl": False
    }

    if operation == "derivative":
        route["solver_strategy"] = "derivative"

    elif operation == "solve":
        route["solver_strategy"] = "equation"

    elif operation == "simplify":
        route["solver_strategy"] = "simplify"

    else:
        route["solver_strategy"] = "simplify"

    return route