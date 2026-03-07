Math Mentor AI

An AI-powered math tutoring system that solves JEE-style math problems using a multi-agent reasoning pipeline, symbolic computation, retrieval-augmented knowledge, and human-in-the-loop feedback.

The system supports text, image, and voice inputs, and explains solutions step-by-step.

Features
Multimodal Input

Text-based math questions

Image upload with OCR extraction

Voice input with speech-to-text

Multi-Agent Reasoning Pipeline

The system uses a structured agent workflow:

Planner

Memory retrieval

Parser

Router

Solver

Verifier

Tutor

Symbolic Math Solving

Uses SymPy for symbolic computation such as:

Derivatives

Equation solving

Expression simplification

Retrieval-Augmented Knowledge (RAG)

A knowledge base of mathematical formulas and rules is indexed with embeddings and retrieved during problem solving.

Vector Memory

Solved problems are stored in FAISS vector memory, allowing the system to reuse solutions for similar problems.

Human-in-the-Loop Feedback

Users can:

Review extracted text

Edit incorrect answers

Provide corrections that update system memory

Observability

The system logs execution steps similar to LangSmith-style tracing, showing how the problem flows through the pipeline.

System Architecture
User Input
(Text / Image / Audio)
        ↓
OCR / Speech Recognition
        ↓
Human Review (HITL)
        ↓
Planner
        ↓
Vector Memory Search (FAISS)
        ↓
Parser → Router → Solver → Verifier → Tutor
        ↓
Knowledge Base Retrieval (RAG)
        ↓
Final Answer + Explanation
        ↓
Memory Store (Self-learning)
Tech Stack
Backend

Python

FastAPI

LangGraph

SymPy

FAISS

Sentence Transformers

Frontend

React

Axios

MediaRecorder API

AI Components

Multi-agent architecture

Symbolic reasoning tools

Retrieval-augmented generation

Vector similarity memory

Project Structure
backend
│
├── agents
│   ├── planner_agent.py
│   ├── parser_agent.py
│   ├── router_agent.py
│   ├── solver_agent.py
│   ├── verifier_agent.py
│   └── tutor_agent.py
│
├── graph
│   └── agent_graph.py
│
├── memory
│   ├── memory_store.py
│   ├── similarity_search.py
│   └── faiss_index.py
│
├── rag
│   ├── retriever.py
│   └── build_index.py
│
├── tools
│   └── sympy_math_tool.py
│
├── observability
│   └── trace_logger.py
│
frontend
│
├── components
│   ├── TextInput.js
│   ├── ImageUpload.js
│   ├── MicrophoneRecorder.js
│   ├── OCRReview.js
│   ├── ResultPanel.js
│   ├── AgentTrace.js
│   └── RAGContext.js
How It Works

The user submits a math problem via text, image, or voice.

OCR or speech recognition converts input into text.

The user reviews the extracted problem.

The planner agent determines the reasoning strategy.

The system checks vector memory for similar problems.

The parser agent extracts the mathematical structure.

The router agent selects the solving strategy.

The solver agent uses SymPy to compute the solution.

The verifier agent checks correctness.

The tutor agent generates step-by-step explanations.

The system stores solved problems for future reuse.

Running Locally
Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend
cd frontend
npm install
npm start
Example Problem

Input

Find derivative of x^2 + 3x

Output

Answer:
2*x + 3

Explanation:
Step 1: Identify the function
Step 2: Apply the power rule
Step 3: Differentiate each term

Confidence: 0.95
Future Improvements

More advanced math parsing

Larger formula knowledge base

Improved vector memory retrieval

Support for more math domains

Interactive reasoning visualization
