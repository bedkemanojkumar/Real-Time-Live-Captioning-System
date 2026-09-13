import numpy as np
from silero_vad import load_silero_vad, get_speech_timestamps


class VoiceActivityDetector:

    def __init__(self, sample_rate=16000):

        self.sample_rate = sample_rate

        print("Loading Silero VAD...")

        self.model = load_silero_vad()

        print("Silero Ready.")

    def contains_speech(self, audio):

        if len(audio) == 0:
            return False

        # Convert (N,1) -> (N,)
        audio = np.squeeze(audio)

        # Ensure float32
        audio = audio.astype(np.float32)

        speech = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate
        )

        return len(speech) > 0