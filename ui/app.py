import streamlit as st
import sounddevice as sd
import numpy as np
import requests
import scipy.io.wavfile as wavfile
import io
import os

# Parameters
SAMPLE_RATE = 16000  # Whisper expects 16kHz mono audio

st.title("Whisper Transcription with RHAIIS")

# Get Whisper URL from environment variable, with default fallback
WHISPER_URL = os.getenv("WHISPER_URL", "http://localhost:8000")
WHISPER_ENDPOINT = WHISPER_URL + "/v1/audio/transcriptions"

# Step 1: Record Audio
duration = st.slider("Select recording duration (seconds)", 1, 10, 5)

if st.button("Record Audio"):
    st.info(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(SAMPLE_RATE * duration), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    st.success("Recording complete.")

    # Step 2: Save to WAV file in memory
    wav_io = io.BytesIO()
    wavfile.write(wav_io, SAMPLE_RATE, audio_data)
    wav_io.seek(0)

    # Step 3: Send to vLLM Whisper endpoint
    st.info(f"Sending audio to Whisper endpoint at: {WHISPER_ENDPOINT}")
    files = {"file": ("audio.wav", wav_io, "audio/wav")}

    try:
        response = requests.post(WHISPER_ENDPOINT, files=files)
        response.raise_for_status()
        result = response.json()
        transcription = result.get("text", "No transcription returned.")
        st.subheader("Transcription")
        st.write(transcription)
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting Whisper endpoint: {e}")
