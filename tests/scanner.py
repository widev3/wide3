# from rtlsdr import RtlSdr
# import numpy as np

# # Initialize device
# sdr = RtlSdr()

# # Configure device
# sdr.sample_rate = 2.4e6  # Hz
# sdr.center_freq = 100e6  # Hz
# sdr.gain = 'auto'

# # Take samples
# samples = sdr.read_samples(256*1024)

# # Process FFT
# fft = np.fft.fftshift(np.fft.fft(samples))
# power = 20*np.log10(np.abs(fft))

# # Cleanup
# sdr.close()


import SoapySDR
from SoapySDR import *  # SOAPY_SDR_ constants
import numpy as np
import matplotlib.pyplot as plt

# ==== Configuration ====
DEVICE_ARGS = dict(driver="rtlsdr")  # change to "rtlsdr" if needed
START_FREQ = 100e6  # Hz
STOP_FREQ = 300e6  # Hz
SAMPLE_RATE = 2.5e6  # Hz (Airspy can do 2.5e6, 3.0e6, 6.0e6, 10e6, etc.)
FFT_SIZE = 1024
STEP = SAMPLE_RATE  # step by bandwidth

# ==== Initialize SDR ====
sdr = SoapySDR.Device(DEVICE_ARGS)
sdr.setSampleRate(SOAPY_SDR_RX, 0, SAMPLE_RATE)
sdr.setGain(SOAPY_SDR_RX, 0, 0)

# ==== Setup stream ====
rxStream = sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32)
sdr.activateStream(rxStream)

freqs = []
powers = []

# ==== Sweep loop ====
for freq in np.arange(START_FREQ, STOP_FREQ, STEP):
    print(f"Tuning to {freq/1e6:.2f} MHz")

    sdr.setFrequency(SOAPY_SDR_RX, 0, freq)

    # Allocate buffer
    buff = np.array([0] * FFT_SIZE, np.complex64)

    # Read samples
    sr = sdr.readStream(rxStream, [buff], len(buff))
    if sr.ret != len(buff):
        print("Warning: sample read incomplete")

    # FFT
    fft = np.fft.fftshift(np.fft.fft(buff))
    power = 20 * np.log10(np.abs(fft))

    # Frequency axis
    f_axis = np.linspace(freq - SAMPLE_RATE / 2, freq + SAMPLE_RATE / 2, FFT_SIZE)

    freqs.extend(f_axis)
    powers.extend(power)

# ==== Cleanup ====
sdr.deactivateStream(rxStream)
sdr.closeStream(rxStream)

# ==== Plot result ====
plt.figure(figsize=(12, 6))
plt.plot(np.array(freqs) / 1e6, powers, lw=0.8)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dB)")
plt.title("Wideband Spectrum Scan")
plt.grid(True)
plt.show(block=True)
