import sounddevice as sd
import soundfile as sf

seconds = 5
sample_rate = 16000

print("Speak now...")

audio = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=1)

sd.wait()

sf.write("my_voice.wav", audio, sample_rate)

print("Saved!")
