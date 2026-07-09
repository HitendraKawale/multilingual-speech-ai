"""
Week 1 · Day 1 — Waveform.
Goal: load an audio file and plot its waveform. Understand sampling rate.

Fill in the TODOs yourself. If you get stuck, ask AI to *explain* the concept —
don't ask it to write the block. Then run:  python day1_waveform.py
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt

AUDIO_PATH = "sample.wav"  # your ~10s recording

# 1) Load the audio.
#    librosa.load returns (y, sr): y = samples (a numpy array), sr = sampling rate.
#    Try sr=None first (keep original), then try sr=16000 and see what changes.
y, sr = librosa.load(AUDIO_PATH, sr=16000)

# TODO A: print the sampling rate, the number of samples (len(y)),
#         and the duration in seconds (len(y) / sr). Confirm the maths yourself.
print(len(y))
print(len(y) / sr)

# TODO B: plot the waveform.
#         Hint: librosa.display.waveshow(y, sr=sr)  — then plt.title/xlabel/ylabel/show.
print(librosa.display.waveshow(y, sr=sr))
plt.title("Waveform")
plt.show()
# TODO C: reload with sr=16000. How many samples now? Why fewer?
#         Write the answer in LEARNINGS.md.

# --- Reflection (answer in LEARNINGS.md, in your own words) ---
# - What does the y-axis (amplitude) represent physically?
# - What does the sampling rate control, and why is 16 kHz common for speech?
