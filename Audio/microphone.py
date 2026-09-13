import queue
import sounddevice as sd


class MicrophoneStream:
    """
    Continuously captures audio from the microphone
    and stores chunks in a thread-safe queue.
    """

    def __init__(
        self,
        sample_rate=16000,
        channels=1,
        block_size=512,
    ):

        self.sample_rate = sample_rate
        self.channels = channels
        self.block_size = block_size

        self.audio_queue = queue.Queue()

        self.stream = None

    def _callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.audio_queue.put(indata.copy())

    def start(self):

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            blocksize=self.block_size,
            callback=self._callback,
        )

        self.stream.start()

        print("🎤 Microphone Started")

    def read(self):

        return self.audio_queue.get()

    def stop(self):

        if self.stream is not None:
            self.stream.stop()
            self.stream.close()

        print("🛑 Microphone Stopped")