import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

sample_rate = 384000  # 192000  # Hz
frequency = 22000  # Hz


def wave(burst, silence):
    t_square = np.linspace(0, burst, int(sample_rate * burst), endpoint=False)
    t_silence = np.linspace(0, silence, int(sample_rate * silence), endpoint=False)
    square_wave = np.sin(2 * np.pi * frequency * t_square)
    silence = np.zeros_like(t_silence)
    return np.concatenate([square_wave, silence])


def zero(message=[]):
    burst = 0.001
    silence = burst / 2
    return np.concatenate([message, wave(burst, silence)])


def one(message=[]):
    silence = 0.001
    burst = silence / 2
    return np.concatenate([message, wave(burst, silence)])


def get_message(bytes: bytes):
    message = []
    bits = [int(bit) for byte in bytes for bit in f"{byte:08b}"]
    for bit in bits:
        print(bit, end="")
        if bit == 0:
            message = zero(message)
        elif bit == 1:
            message = one(message)

    print()

    return message


diseqc_command = [0xE0, 0x10, 0x38, 0xF0]
message = get_message(diseqc_command)

print("Playing")
sd.play(message, sample_rate)
sd.wait()

# plt.ion()
# plt.figure(figsize=(10, 4))
# plt.plot(np.arange(len(message)) / sample_rate * 1000, message)
# plt.title(f"DiSEqC message of {diseqc_command}")
# plt.xlabel("Time (ms)")
# plt.ylabel("Amplitude")
# plt.grid(True)
# plt.tight_layout()
# plt.show(block=True)
