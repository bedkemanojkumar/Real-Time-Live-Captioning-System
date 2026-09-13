from audio.microphone import MicrophoneStream
from audio.buffer import AudioBuffer
from audio.speech_buffer import SpeechBuffer
from audio.vad import VoiceActivityDetector
from asr.whisper_engine import WhisperEngine
from core.states import PipelineState


class LiveCaptionPipeline:

    def __init__(self, caption_queue=None):

        # Thread-safe queue for caption routing (e.g., Streamlit worker thread)
        self.caption_queue = caption_queue

        # Controls pipeline loop
        self.running = False

        # Audio Input
        self.microphone = MicrophoneStream()

        # Rolling window for VAD
        self.buffer = AudioBuffer(max_chunks=50)

        # Complete speech segment
        self.speech_buffer = SpeechBuffer()

        # AI Models
        self.vad = VoiceActivityDetector()
        self.whisper = WhisperEngine()

        # Initial state
        self.state = PipelineState.LISTENING

    def stop(self):
        """Stop the pipeline loop and release microphone resources."""
        self.running = False
        self.microphone.stop()

    def start(self):

        print("=" * 60)
        print(" Live Caption AI Started")
        print("=" * 60)

        print(f"Current State : {self.state.value}")

        self.microphone.start()

        try:

            self.running = True
            while self.running:

                # ------------------------------------
                # Read microphone chunk
                # ------------------------------------
                chunk = self.microphone.read()

                # Always update rolling buffer
                self.buffer.add(chunk)

                # While recording, store every chunk
                if self.state == PipelineState.RECORDING:
                    self.speech_buffer.add(chunk)

                print(
                    f"\rState: {self.state.value} | Rolling Buffer: {self.buffer.size()}",
                    end=""
                )

                # Wait until rolling window is full
                if self.buffer.size() < self.buffer.max_chunks:
                    continue

                # Get current rolling audio
                audio = self.buffer.get_audio()

                # Detect speech
                speech = self.vad.contains_speech(audio)

                # ------------------------------------
                # LISTENING -> RECORDING
                # ------------------------------------
                if speech:

                    if self.state == PipelineState.LISTENING:

                        self.state = PipelineState.RECORDING

                        print("\n\nSpeech Detected!")

                        # Start a fresh speech segment
                        self.speech_buffer.clear()

                        # Save the current rolling window
                        # so initial words are not lost
                        self.speech_buffer.add(audio)

                # ------------------------------------
                # RECORDING -> TRANSCRIBING
                # ------------------------------------
                else:

                    if self.state == PipelineState.RECORDING:

                        self.state = PipelineState.TRANSCRIBING

                        print("\nSpeech Ended")

                        print("Transcribing...")

                        speech_audio = self.speech_buffer.get_audio()

                        if len(speech_audio) > 0:

                            result = self.whisper.transcribe_audio(
                                speech_audio
                            )

                            caption_text = result.get("text", "").strip()

                            if caption_text:
                                if self.caption_queue is not None:
                                    self.caption_queue.put(caption_text)
                                else:
                                    # Preserve existing terminal markers when no queue is used
                                    print("\n" + "=" * 50)
                                    print("LIVE CAPTION")
                                    print("=" * 50)
                                    print(caption_text)
                                    print("=" * 50)

                        self.speech_buffer.clear()

                        self.state = PipelineState.LISTENING

                        print("\nListening Again...\n")

                # Clear rolling window
                self.buffer.clear()

        except KeyboardInterrupt:

            print("\nStopping Pipeline...")

            self.microphone.stop()

