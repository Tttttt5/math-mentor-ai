import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

import streamlit as st
from graph.agent_graph import run_math_pipeline
import easyocr
import speech_recognition as sr
from audiorecorder import audiorecorder
import tempfile


st.title("Math Mentor AI")

st.write("Solve math problems using text, image OCR, or voice.")

mode = st.radio(
    "Choose input method",
    ["Text", "Image", "Microphone"]
)

input_text = ""

# TEXT INPUT
if mode == "Text":

    input_text = st.text_input("Enter your math problem")


# IMAGE OCR
elif mode == "Image":

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        reader = easyocr.Reader(['en'])

        with tempfile.NamedTemporaryFile(delete=False) as tmp:

            tmp.write(uploaded_file.read())

            result = reader.readtext(tmp.name)

        extracted = " ".join([r[1] for r in result])

        st.subheader("Extracted Text")

        input_text = st.text_area(
            "Review and edit",
            extracted
        )


# MICROPHONE
elif mode == "Microphone":

    audio = audiorecorder(
        "Click to record",
        "Recording..."
    )

    if len(audio) > 0:

        st.audio(audio.export().read())

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:

            audio.export(f.name, format="wav")

            recognizer = sr.Recognizer()

            with sr.AudioFile(f.name) as source:

                audio_data = recognizer.record(source)

                try:

                    input_text = recognizer.recognize_google(audio_data)

                except:

                    st.error("Speech recognition failed")

        st.text_area(
            "Transcribed text",
            input_text
        )


# SOLVE
if st.button("Solve"):

    if input_text.strip() == "":

        st.warning("Please provide a problem")

    else:

        result = run_math_pipeline(input_text)

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