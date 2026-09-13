import os

print("=" * 70)
print("DEBUG: pipeline_runner.py loaded")
print(f"File Path: {os.path.abspath(__file__)}")
print("=" * 70)

import threading
import queue



from core.pipeline import LiveCaptionPipeline



class PipelineRunner:

    def __init__(self):

        print(f">>> PipelineRunner.__init__() called | id={id(self)}")

        print(f">>> PipelineRunner created | id={id(self)}")


        self.caption_queue = queue.Queue()

        # Lazy loading:
        # Do not construct LiveCaptionPipeline (and therefore WhisperModel)
        # during Streamlit page import.
        self.pipeline = None

        self.thread = None
        self._lock = threading.Lock()

    def start(self):

        print(f">>> PipelineRunner.start() called | id={id(self)}")

        with self._lock:

            # Instantiate the pipeline only when the user clicks Start.
            if self.pipeline is None:

                print(">>> Creating LiveCaptionPipeline...")

                self.pipeline = LiveCaptionPipeline(
                    caption_queue=self.caption_queue
                )

                print(">>> LiveCaptionPipeline created successfully.")


            if self.thread is None or not self.thread.is_alive():

                print(">>> Creating pipeline thread...")

                self.thread = threading.Thread(
                    target=self.pipeline.start,
                    daemon=True
                )

                print(">>> Starting pipeline thread...")

                self.thread.start()

                print(">>> Pipeline thread started successfully.")
            else:
                print(">>> Pipeline thread is already running.")



    def stop(self):

        print(f">>> PipelineRunner.stop() called | id={id(self)}")


        if self.pipeline is not None:
            self.pipeline.stop()

    def get_queue(self):

        return self.caption_queue

