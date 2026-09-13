# 🎤 Live Caption AI

An AI-powered speech-to-text application that captures microphone audio, detects speech, transcribes it using Faster Whisper, and displays live captions through a Streamlit interface.

The project is designed with a modular architecture for audio processing, automatic speech recognition, caption pipelines, transcript handling, and export services.

## Project Overview

Live Caption AI converts spoken audio into text using an offline speech-recognition pipeline.

The application uses:

* Microphone audio capture
* Audio buffering
* Speech buffering
* Voice Activity Detection using Silero VAD
* Speech recognition using Faster Whisper
* Caption pipeline management
* Streamlit-based user interface
* Transcript history
* Translation and summarization services
* Transcript storage
* DOCX, PDF, and SRT export support

## Main Workflow

```text
Microphone Input
       ↓
Audio Capture
       ↓
Audio Buffering
       ↓
Voice Activity Detection
       ↓
Speech Segment Detection
       ↓
Faster Whisper ASR
       ↓
Text Transcription
       ↓
Caption Pipeline
       ↓
Streamlit UI
       ↓
Transcript History / Export
```

## Key Features

### 🎙️ Audio Processing

The audio module handles microphone input and audio buffering.

It includes:

* Microphone capture
* Audio buffer management
* Speech buffer management
* Voice Activity Detection

### 🧠 Automatic Speech Recognition

The project uses **Faster Whisper** for speech-to-text conversion.

The Whisper engine:

* Accepts audio data
* Converts the audio into a temporary WAV file
* Transcribes the audio
* Returns the recognized text
* Returns detected language information
* Returns language probability information

The default Whisper configuration uses:

```text
Model: small
Device: CPU
Compute type: int8
Beam size: 5
```

### 🟢 Voice Activity Detection

Silero VAD is used to identify speech activity in the incoming audio.

This helps the pipeline distinguish between:

* Speech
* Silence
* Non-speech audio

### 🖥️ Streamlit User Interface

The application includes a Streamlit interface with:

* Start Listening button
* Stop Listening button
* Clear Transcript button
* Current listening status
* Live caption display
* Transcript history

### 📄 Export Services

The project includes export modules for:

* DOCX
* PDF
* SRT subtitle files

### 🌐 Additional Services

The services module contains functionality for:

* Transcript export
* Text summarization
* Translation

### 💾 Storage

The storage module is responsible for transcript database functionality.

## Project Architecture

```text
Live-Caption-AI/
│
├── asr/
│   └── whisper_engine.py
│
├── audio/
│   ├── buffer.py
│   ├── microphone.py
│   ├── speech_buffer.py
│   └── vad.py
│
├── core/
│   ├── events.py
│   ├── pipeline.py
│   ├── states.py
│   ├── test_buffer.py
│   ├── test_microphone.py
│   ├── test_vad.py
│   └── test_whisper.py
│
├── export/
│   ├── docx_export.py
│   ├── pdf_export.py
│   └── srt_export.py
│
├── services/
│   ├── export.py
│   ├── summary.py
│   └── translate.py
│
├── storage/
│   └── transcript_db.py
│
├── ui/
│   ├── app.py
│   └── pipeline_runner.py
│
├── config.py
├── main.py
├── README.md
└── requirements.txt
```

## Technologies Used

* Python
* Faster Whisper
* Whisper
* Silero VAD
* Streamlit
* PyTorch
* TorchAudio
* NumPy
* SciPy
* SoundFile
* ReportLab
* Python-DOCX
* Transformers
* Hugging Face Hub

## Installation

Clone the repository:

```bash
git clone https://github.com/bedkemanojkumar/Live-Caption-AI.git
```

Move into the project directory:

```bash
cd Live-Caption-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

### Run the main pipeline

```bash
python main.py
```

### Run the Streamlit interface

From the project root, run:

```bash
streamlit run ui/app.py
```

The Streamlit application will open in your browser.

## Usage

1. Install the required dependencies.
2. Connect or select a working microphone.
3. Start the Streamlit application.
4. Click **Start Listening**.
5. Speak through the microphone.
6. View the generated captions in the interface.
7. Click **Stop Listening** to stop the process.
8. Review the transcript history.
9. Use the available export services when required.

## ASR Configuration

The Whisper engine is configured with the following default settings:

```python
WhisperEngine(
    model_size="small",
    device="cpu",
    compute_type="int8"
)
```

You can modify the model configuration depending on your hardware.

For example:

* Smaller models require fewer resources.
* Larger models may provide improved transcription quality.
* CPU execution is supported.
* GPU execution may be configured when compatible hardware is available.

## Testing

The project contains test files for important components, including:

* Audio buffer
* Microphone
* Voice Activity Detection
* Whisper transcription

Test files are located inside the `core/` directory.

## Important Notes

* A working microphone is required for live audio capture.
* The first Whisper model execution may require model files to be downloaded.
* Transcription speed depends on the selected model and available hardware.
* CPU inference may be slower than GPU inference.
* Audio and recording files should not be uploaded to GitHub unless they are intentionally included as sample data.
* Do not upload API keys, passwords, private recordings, or other sensitive information.

## Future Improvements

Potential improvements include:

* Improved real-time caption refresh
* Better background-thread handling
* Speaker identification
* Multilingual caption support
* Automatic punctuation improvement
* Noise reduction
* Caption confidence visualization
* Word-level timestamps
* Better transcript search
* Real-time translation
* Improved subtitle synchronization
* Cloud deployment
* Docker support
* More comprehensive automated tests

## Learning Outcomes

This project helped explore:

* Speech-to-text systems
* Automatic Speech Recognition
* Audio signal processing
* Voice Activity Detection
* Whisper-based transcription
* Modular Python architecture
* Streamlit application development
* Transcript processing
* File export systems
* Database-backed storage
* AI service integration

## Author

**Manojkumar Shriniwas Bedke**

* GitHub: https://github.com/bedkemanojkumar
* LinkedIn: https://www.linkedin.com/in/manojkumar-bedke01/
