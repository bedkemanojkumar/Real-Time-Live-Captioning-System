import numpy as np


class AudioBuffer:
    """
    Rolling audio buffer.
    Stores only the latest N chunks.
    """

    def __init__(self, max_chunks=50):

        self.max_chunks = max_chunks
        self.chunks = []

    def add(self, chunk):

        chunk = np.asarray(chunk).flatten().astype(np.float32)
        self.chunks.append(chunk)

        if len(self.chunks) > self.max_chunks:
            self.chunks.pop(0)

    def get_audio(self):

        if len(self.chunks) == 0:
            return np.array([], dtype=np.float32)

        return np.concatenate(self.chunks, axis=0).flatten()

    def clear(self):
        self.chunks.clear()

    def size(self):
        return len(self.chunks)

    def empty(self):
        return len(self.chunks) == 0