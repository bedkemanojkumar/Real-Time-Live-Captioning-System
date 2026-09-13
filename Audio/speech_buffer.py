import numpy as np


class SpeechBuffer:
    """
    Stores one complete speech segment.
    """

    def __init__(self):
        self.chunks = []

    def add(self, chunk):

        # Convert everything to a flat float32 array
        chunk = np.asarray(chunk).flatten().astype(np.float32)

        self.chunks.append(chunk)

    def clear(self):
        self.chunks.clear()

    def empty(self):
        return len(self.chunks) == 0

    def get_audio(self):

        if self.empty():
            return np.array([], dtype=np.float32)

        return np.concatenate(self.chunks)

    def size(self):
        return len(self.chunks)