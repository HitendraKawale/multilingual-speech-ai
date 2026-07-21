import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# still ...

audio, sr = librosa.load("my_voice.wav", sr=16000)


print(audio.shape)
print(sr)


mel = librosa.feature.melspectrogram(y=audio, sr=sr)


mel_db = librosa.power_to_db(mel, ref=np.max)


plt.figure(figsize=(10, 4))

librosa.display.specshow(mel_db, sr=sr, x_axis="time", y_axis="mel")

plt.colorbar()

plt.title("My Voice as AI sees it")

plt.show()
