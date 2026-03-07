def generate_explanation(problem, solution, rag_context=None):

    explanation = f"""
Step 1: Identify the mathematical expression.

Step 2: Apply the appropriate rule.

Step 3: Simplify the result.

Final Answer: {solution}
"""

    if rag_context:

        explanation += "\n\nRelevant Knowledge:\n"

        for ctx in rag_context[:2]:

            explanation += f"\n- {ctx[:200]}..."

    return explanation