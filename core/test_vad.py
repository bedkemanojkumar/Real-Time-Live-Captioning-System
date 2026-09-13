import soundfile as sf

from audio.vad import VoiceActivityDetector


vad = VoiceActivityDetector()

audio, sr = sf.read("recordings/test.wav")

print("Contains Speech :", vad.contains_speech(audio))