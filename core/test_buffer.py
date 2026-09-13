import numpy as np

from audio.buffer import AudioBuffer

buffer = AudioBuffer()

for i in range(5):

    chunk = np.random.rand(512, 1).astype("float32")

    buffer.add(chunk)

print("Chunks :", buffer.size())

audio = buffer.get_audio()

print("Merged shape :", audio.shape)

buffer.clear()

print("Chunks after clear :", buffer.size())  