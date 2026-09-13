from enum import Enum


class PipelineState(Enum):
    LISTENING = "LISTENING"
    RECORDING = "RECORDING"
    TRANSCRIBING = "TRANSCRIBING"