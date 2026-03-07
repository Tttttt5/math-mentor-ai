from typing import TypedDict, Optional, Dict, List
from langgraph.graph import StateGraph, END

from agents.parser_agent import parse_problem
from agents.router_agent import route_problem
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution
from agents.tutor_agent import generate_explanation

from memory.memory_store import store_problem
from memory.similarity_search import find_similar_problem

from observability.trace_logger import TraceLogger
from agents.planner_agent import plan_solution

trace = TraceLogger()


class MathState(TypedDict):

    question: str

    parsed_problem: Optional[Dict]

    route: Optional[Dict]

    expression: Optional[str]

    solution: Optional[str]

    rag_context: Optional[List[str]]

    verification: Optional[Dict]

    explanation: Optional[str]


# MEMORY SEARCH NODE
def memory_lookup_node(state: MathState):

    trace.log("Memory Lookup")

    question = state["question"]

    similar = find_similar_problem(question)

    if similar:

        return {
            "solution": similar[1],
            "rag_context": ["Retrieved from memory"]
        }

    return {}


# PARSER
def parser_node(state: MathState):

    trace.log("Parser Agent")

    parsed = parse_problem(state["question"])

    return {"parsed_problem": parsed}


# ROUTER
def router_node(state: MathState):

    trace.log("Router Agent")

    route = route_problem(state["parsed_problem"])

    return {"route": route}


# SOLVER
def solver_node(state: MathState):

    trace.log("Solver Agent")

    result = solve_problem(state["parsed_problem"], state["route"])

    return {
        "expression": result["expression"],
        "solution": result["solution"],
        "rag_context": result["rag_context"]
    }


# VERIFIER
def verifier_node(state: MathState):

    trace.log("Verifier Agent")

    verification = verify_solution(
        state["expression"],
        state["solution"],
        state["parsed_problem"]["operation"]
    )

    return {"verification": verification}


# TUTOR
def tutor_node(state: MathState):

    trace.log("Tutor Agent")

    explanation = generate_explanation(
        state["question"],
        state["solution"]
    )

    return {"explanation": explanation}


# MEMORY STORE
def memory_store_node(state: MathState):

    trace.log("Memory Store")

    store_problem(
        state["question"],
        state["solution"]
    )

    return {}

def planner_node(state):

    plan = plan_solution(state["question"])

    return {"plan": plan}

workflow = StateGraph(MathState)

workflow.add_node("memory_lookup", memory_lookup_node)
workflow.add_node("parser", parser_node)
workflow.add_node("router", router_node)
workflow.add_node("solver", solver_node)
workflow.add_node("verifier", verifier_node)
workflow.add_node("tutor", tutor_node)
workflow.add_node("memory_store", memory_store_node)

workflow.set_entry_point("memory_lookup")

workflow.add_edge("memory_lookup", "parser")
workflow.add_edge("parser", "router")
workflow.add_edge("router", "solver")
workflow.add_edge("solver", "verifier")
workflow.add_edge("verifier", "tutor")
workflow.add_edge("tutor", "memory_store")
workflow.add_edge("memory_store", END)
workflow.add_node("planner", planner_node)
workflow.set_entry_point("planner")

workflow.add_edge("planner", "memory_lookup")
math_graph = workflow.compile()


def run_math_pipeline(question):

    trace.events = []   # reset trace

    result = math_graph.invoke({"question": question})

    return {
        "question": question,
        "answer": result.get("solution"),
        "explanation": result.get("explanation"),
        "confidence": result.get("verification", {}).get("confidence", 0.8),
        "rag_context": result.get("rag_context", []),
        "trace": trace.get_trace()
    }