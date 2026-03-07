import os
import uuid
import subprocess
from faster_whisper import WhisperModel

# Create temp directory
TEMP_DIR = "temp_audio"
os.makedirs(TEMP_DIR, exist_ok=True)

# Load whisper model once at startup
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def convert_to_wav(input_path):
    """
    Convert any audio format (webm) to clean WAV
    """

    wav_path = os.path.join(TEMP_DIR, f"{uuid.uuid4()}.wav")

    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ac",
        "1",
        "-ar",
        "16000",
        wav_path
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return wav_path


def transcribe_audio(file_path):
    """
    Convert audio → text using faster-whisper
    """

    # Convert webm to wav
    wav_path = convert_to_wav(file_path)

    segments, info = model.transcribe(wav_path)

    text_segments = []

    for segment in segments:
        text_segments.append(segment.text)

    transcript = " ".join(text_segments).strip()

    # cleanup
    if os.path.exists(wav_path):
        os.remove(wav_path)

    return transcript