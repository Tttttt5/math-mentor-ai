from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from agents.asr_agent import transcribe_audio
from agents.ocr_agent import extract_text_from_image
from graph.agent_graph import run_math_pipeline
from memory.memory_store import store_corrected_solution
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = "temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "AI Math Mentor API running"}


# TEXT INPUT → SOLVER
@app.post("/solve")
async def solve_problem(data: dict):

    text = data.get("content")

    result = run_math_pipeline(text)

    return result


# IMAGE OCR
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    file_path = os.path.join(TEMP_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_image(file_path)

    os.remove(file_path)

    return {
        "extracted_text": extracted_text
    }


# AUDIO → SPEECH TO TEXT
@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):

    file_path = os.path.join(TEMP_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)

    os.remove(file_path)

    return {
        "extracted_text": transcript
    }

@app.post("/feedback")
async def feedback(data: dict):

    question = data["question"]
    corrected_answer = data["corrected_answer"]

    store_corrected_solution(question, corrected_answer)

    return {"status": "stored"}