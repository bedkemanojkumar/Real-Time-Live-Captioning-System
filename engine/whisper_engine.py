import tempfile
import os

import soundfile as sf
from faster_whisper import WhisperModel


class WhisperEngine:

    def __init__(
        self,
        model_size="small",
        device="cpu",
        compute_type="int8"
    ):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

        print("Whisper Ready.")

    def transcribe_audio(self, audio, sample_rate=16000):
        """
        audio : numpy array (float32)
        returns : transcript string
        """

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as tmp:

            temp_path = tmp.name

        try:

            sf.write(temp_path, audio, sample_rate)

            segments, info = self.model.transcribe(
                temp_path,
                beam_size=5
            )

            text = " ".join(
                segment.text.strip()
                for segment in segments
            )

            return {
                "text": text,
                "language": info.language,
                "probability": info.language_probability
            }

        finally:

            if os.path.exists(temp_path):
                os.remove(temp_path)