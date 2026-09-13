from audio.microphone import MicrophoneStream

mic = MicrophoneStream()

mic.start()

while True:

    chunk = mic.read()

    print(chunk.shape)