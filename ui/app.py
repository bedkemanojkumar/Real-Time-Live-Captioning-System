import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from pipeline_runner import PipelineRunner
# from streamlit_autorefresh import st_autorefresh
#
# st_autorefresh(interval=500, key="caption_refresh")

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="Live Caption AI",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.write("✅ Step 1: Streamlit page loaded")

# ---------------------------------------
# Session State Initialization
# ---------------------------------------
if "running" not in st.session_state:
    st.session_state.running = False

if "caption" not in st.session_state:
    st.session_state.caption = "Waiting for speech..."

if "history" not in st.session_state:
    st.session_state.history = []

if "runner" not in st.session_state:
    # NOTE: No callback architecture.
    # The UI will consume captions from runner.get_queue() on each rerun.
    st.write("✅ Step 2: Creating PipelineRunner")
    st.session_state.runner = PipelineRunner()
    st.write("✅ Step 3: PipelineRunner created")

# ---------------------------------------
# Drain caption queue (main thread only)
# ---------------------------------------
st.write("✅ Step 4: Checking caption queue")
# Streamlit reruns the script top-to-bottom on interaction.
# Every rerun must read captions from the queue and update session_state.
try:
    caption_queue = st.session_state.runner.get_queue()

    st.write(f"Queue Size: {caption_queue.qsize()}")

    while not caption_queue.empty():
        caption = caption_queue.get()
        st.write(f"Received Caption: {caption}")
        st.session_state.caption = caption
        st.session_state.history.append(caption)
except Exception:
    # Keep UI stable even if the runner isn't ready yet.
    pass

# ---------------------------------------
# Sidebar
# ---------------------------------------
with st.sidebar:

    st.title("🎤 Live Caption AI")

    st.markdown("---")

    st.subheader("Project")

    st.write("""
    Offline Speech-to-Text

    • Silero VAD
    • Faster Whisper
    • Streamlit
    """)

    st.markdown("---")

    if st.session_state.running:
        st.success("🟢 Listening")
    else:
        st.error("🔴 Stopped")

# ---------------------------------------
# Header
# ---------------------------------------
st.title("🎤 Live Caption Generation")

st.caption(
    "Offline Speech Recognition using Silero VAD + Faster Whisper"
)

st.divider()

# ---------------------------------------
# Layout
# ---------------------------------------
left, right = st.columns([1, 3])

# ---------------------------------------
# Controls
# ---------------------------------------
with left:

    st.subheader("Controls")

    if st.button("▶ Start Listening", use_container_width=True):
        st.write("✅ Start button clicked")
        print(">>> Start button clicked")
        st.session_state.running = True
        st.session_state.caption = "Listening..."

    if st.button("■ Stop Listening", use_container_width=True):
        st.write("🛑 Stop button clicked")
        print(">>> Stop button clicked")
        st.session_state.running = False
        st.session_state.caption = "Stopped."


    if st.button("🗑 Clear Transcript", use_container_width=True):
        st.session_state.history = []

    st.write(f"Running State = {st.session_state.running}")
    print(f">>> running = {st.session_state.running}")

    if st.session_state.running:

        st.write("Calling runner.start()")
        print(">>> About to call runner.start()")

        st.session_state.runner.start()

        st.write("runner.start() finished")
        print(">>> runner.start() returned")

    else:

        st.write("Calling runner.stop()")
        print(">>> About to call runner.stop()")

        st.session_state.runner.stop()

        st.write("runner.stop() finished")
        print(">>> runner.stop() returned")



    st.markdown("---")

    st.subheader("Current State")

    if st.session_state.running:
        st.success("LISTENING")
    else:
        st.error("STOPPED")

# ---------------------------------------
# Live Caption
# ---------------------------------------
with right:

    st.subheader("Live Caption")
    st.info(st.session_state.caption)

# ---------------------------------------
# Transcript
# ---------------------------------------
st.divider()

st.subheader("📜 Transcript History")

if len(st.session_state.history) == 0:
    st.info("No transcript available.")
else:
    for sentence in reversed(st.session_state.history):
        st.write("•", sentence)

st.write("✅ Step 5: UI rendering completed")

