def plan_solution(question: str):

    q = question.lower()

    plan = {
        "use_memory": True,
        "use_rag": False,
        "solver_type": "symbolic"
    }

    if "derivative" in q or "integral" in q or "limit" in q:
        plan["solver_type"] = "calculus"

    if "probability" in q:
        plan["solver_type"] = "probability"
        plan["use_rag"] = True

    if "theory" in q or "explain" in q:
        plan["solver_type"] = "conceptual"
        plan["use_rag"] = True

    return plan