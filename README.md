# 🗣️ Whisper Transcription App (Streamlit + RHAIIS)

This Streamlit-based application allows users to record audio directly in the browser, send the recording to a Whisper-compatible API endpoint, and view the transcription. It integrates easily with a local or remote Whisper backend, such as OpenAI Whisper, vLLM, or RHAIIS.

---

## 📦 Features

- Record audio from the browser
- Send audio to a Whisper transcription endpoint
- View transcribed text directly in the app
- Adjustable recording duration (1–10 seconds)

---

## ⚙️ Installation

### 1. Set Up a Python Environment

Ensure you are using Python 3.8 or higher. It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Dependencies

```bash
cd ui
```

Install all required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

### 1. Set the Whisper API Endpoint

Configure the API endpoint by setting the `WHISPER_URL` environment variable:

```bash
export WHISPER_URL=http://your-whisper-api.com  # or http://localhost:8000
```

> If this is not set, the app defaults to `http://localhost:8000`.

### 2. Launch the Streamlit App

Run the app using Streamlit:

```bash
streamlit run app.py
```

> Replace `app.py` with your actual script filename if different.

---

## 🧪 Using the App

1. Open the Streamlit app in your browser (usually at [http://localhost:8501](http://localhost:8501))
2. Use the slider to select a recording duration (between 1 and 10 seconds)
3. Click **"Record Audio"**
4. The app will:
   - Capture your voice input
   - Save and send a WAV file to the Whisper API
   - Display the transcribed text from the response

---

## 🛠️ Troubleshooting

- **Microphone Permission Issues**: Grant permission for microphone access when prompted.
- **Connection Errors**: Ensure the `WHISPER_URL` is correct and the endpoint is running.
- **Dependency Errors**: Run `pip install -r requirements.txt` again to verify packages are installed.
- **Port Conflicts**: If port 8501 is occupied, specify an alternative port:

  ```bash
  streamlit run app.py --server.port 8502
  ```

---

## 🧠 Notes

- The Whisper endpoint should accept POST requests at `/v1/audio/transcriptions` with a file upload field named `file`.
- Audio is recorded in 16kHz mono format, as expected by Whisper.
- This setup is ideal for testing Whisper models running on vLLM or similar deployments.

