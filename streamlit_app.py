import streamlit as st
from graph.agent_graph import run_math_pipeline

st.title("Math Mentor AI")

st.write("Solve JEE-style math problems with AI reasoning.")

question = st.text_input("Enter a math question")

if st.button("Solve"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        result = run_math_pipeline(question)

        st.subheader("Answer")
        st.write(result.get("answer"))

        st.subheader("Explanation")
        st.write(result.get("explanation"))

        st.subheader("Confidence")
        st.write(result.get("confidence"))

        if result.get("rag_context"):
            st.subheader("Knowledge Context")
            for ctx in result["rag_context"]:
                st.write(ctx)

        if result.get("trace"):
            st.subheader("Execution Steps")
            for step in result["trace"]:
                st.write(step)