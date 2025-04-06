🎙️ Audio Transcription Script (with Whisper)
This script allows you to transcribe audio files (like .wav or .mp3) using OpenAI’s Whisper model.

📋 What It Does
Converts audio into text using the faster-whisper library.

Shows start and end timestamps for each segment of the audio.

🚀 How to Use It (Step-by-Step)
✅ 1. Clone this repo and go into the folder:

git clone https://github.com/Vagabond3344/Python.git

cd Python

✅ 2. Create a Python Virtual Environment
This keeps dependencies clean and separate from your system Python.

On Windows:
python -m venv venv
venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

✅ 3. Install the required packages
Make sure your virtual environment is activated, then run:

pip install faster-whisper
pip install ffmpeg-python

You also need FFmpeg installed on your system:

On Windows:

Download and install from https://ffmpeg.org/download.html

Add ffmpeg/bin to your system PATH

On macOS:
brew install ffmpeg

On Linux (Ubuntu/Debian):
sudo apt install ffmpeg

✅ 4. Run the transcription script
Replace name_of_file.py with the name of your script and audiofile.mp3 with your actual audio file:
python name_of_file.py path/to/audiofile.mp3

Example:
python transcribe.py samples/audio.wav

🧠 How It Works
Loads the Whisper model (base) using faster-whisper.
Transcribes the audio in segments.
Prints each segment’s timestamp and text to the console.

Example Output:
[0.00s - 3.45s] Hello, how are you?
[3.45s - 6.00s] I'm testing this transcription tool.

🧰 Dependencies
These will be installed with pip:
faster-whisper
ffmpeg-python

And you need to install FFmpeg separately (see above ⬆️).

🆘 Help
If you get any errors, double-check:
Your audio file path is correct.
You’ve activated your virtual environment.
FFmpeg is installed and added to your system PATH.
