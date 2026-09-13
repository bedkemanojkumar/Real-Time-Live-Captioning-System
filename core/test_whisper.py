import soundfile as sf

from asr.whisper_engine import WhisperEngine

whisper = WhisperEngine()

audio, sr = sf.read("recordings/test.wav")

result = whisper.transcribe_audio(audio, sr)

print(result)