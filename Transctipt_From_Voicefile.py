# Transcript from voice file
# use : python3 *nameoffile.py* *file location*

import argparse
from faster_whisper import WhisperModel

def transcribe_audio(file_path):
    # Initialize the model
    model = WhisperModel("base", compute_type="int8")

    # Transcribe the audio file
    segments, info = model.transcribe(file_path)

    # Print the transcribed text
    for segment in segments:
        print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}")

if __name__ == "__main__":
    # Set up argument parser to accept file path from the command line
    parser = argparse.ArgumentParser(description="Transcribe audio from a file.")
    parser.add_argument("file_path", help="Path to the audio file (e.g., .wav, .mp3)")

    # Parse the arguments
    args = parser.parse_args()

    # Call the transcription function
    transcribe_audio(args.file_path)
