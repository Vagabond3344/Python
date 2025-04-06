import sounddevice as sd
import numpy as np
import queue
import threading
import whisper
import torch
import time

# Set model
model = whisper.load_model("base")  # You can switch to "small", "medium", etc.

# Audio recording settings
SAMPLE_RATE = 16000
CHUNK_DURATION = 6  # seconds
OVERLAP_DURATION = 3  # seconds (increased overlap)
SILENCE_THRESHOLD = 0.05  # Volume threshold to detect silence (increase threshold)
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)
OVERLAP_SIZE = int(SAMPLE_RATE * OVERLAP_DURATION)

q = queue.Queue()
buffer = np.zeros((0,), dtype=np.float32)
last_transcription = ""

print("\n[Transcription Started] 🎙️ Speak into your mic...")

def callback(indata, frames, time_info, status):
    if status:
        print(status, flush=True)
    q.put(indata[:, 0].copy())

def record_audio():
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback):
        while True:
            try:
                data = q.get()
                global buffer
                buffer = np.concatenate((buffer, data))

                # If enough data is collected
                if len(buffer) >= CHUNK_SIZE:
                    chunk = buffer[:CHUNK_SIZE]
                    buffer = buffer[CHUNK_SIZE - OVERLAP_SIZE:]  # Keep overlap

                    # Check for silence
                    if np.max(np.abs(chunk)) > SILENCE_THRESHOLD:
                        # Start transcription in a separate thread
                        threading.Thread(target=transcribe_audio, args=(chunk,)).start()
            except Exception as e:
                print(f"[ERROR] {e}")
                break

def transcribe_audio(audio_chunk):
    global last_transcription
    try:
        # Pad or trim the audio chunk to fit Whisper's input requirements
        audio = whisper.pad_or_trim(audio_chunk)
        
        # Convert to mel spectrogram
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # Set decoding options with the FP16 flag if CUDA is available
        options = whisper.DecodingOptions(fp16=torch.cuda.is_available(), language="en")
        
        # Decode the audio into text
        result = whisper.decode(model, mel, options)

        transcription = result.text.strip()

        # Only print new transcriptions (avoid repeating the same result)
        if transcription and transcription != last_transcription:
            print(f"\n📝 {transcription}")
            last_transcription = transcription

    except Exception as e:
        print(f"[ERROR during transcription] {e}")

try:
    record_audio()
except KeyboardInterrupt:
    print("\n[Stopping transcription]")
    exit()

