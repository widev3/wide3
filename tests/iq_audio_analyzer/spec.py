import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

fs, data = wavfile.read("recording.wav")
data = data.astype(np.float32)
iq = data[:, 0] + 1j * data[:, 1]
f, t, Sxx = spectrogram(iq, fs=fs, window="hann", nperseg=1024, noverlap=512)

plt.ion()
plt.figure(figsize=(10, 6))
plt.imshow(
    np.fft.fftshift(10 * np.log10(np.abs(Sxx)), axes=0),
    aspect="auto",
    extent=[f[0] - fs / 2, f[-1] - fs / 2, t[-1], t[0]],  # X=freq, Y=time
    cmap="inferno",
)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Time (s)")
plt.title("Spectrogram of IQ Recording")
plt.colorbar(label="Power (dB)")
plt.show(block=True)
